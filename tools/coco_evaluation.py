################################################################################
# Example : Coco evaluation for object detection
# using different object tracking algorithms.
# Copyright (c) 2024 - Neelanjan Bhowmik
# Durham University, UK
# License : 
################################################################################

import json
from typing import Union, List
import numpy as np
import os
import argparse
import io
from contextlib import redirect_stdout

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval, Params

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
from matplotlib import pyplot as plt

################################################################################

def csv_write(out_csv_filename,
    summary_all):

    with open(out_csv_filename, 'w') as file:
    # Loop through the list and write each string to the file
        for string in summary_all:
            file.write(string + "\n")

################################################################################

class DetectionPerformanceEvaluation:

    def __init__(self, gt: Union[str, COCO], prediction: Union[List, str], params=None, th=0.5):
        if isinstance(gt, str):
            ff = io.StringIO()
            with redirect_stdout(ff):
                gt = COCO(gt)
        
        prediction_coco = dict()
        if isinstance(prediction, str):
            
            # ff = io.StringIO()
            # with redirect_stdout(ff):
            prediction = json.load(open(prediction, 'r'))  # Loading the json file as an array of dicts
            assert type(prediction) == list, 'annotation file format {} not supported'.format(
                type(prediction))
            
        for i, p in enumerate(prediction):
            p['id'] = i
            p['area'] = p['bbox'][2] * p['bbox'][3]
        # Adding these lines I give the detection file the xray format
        prediction_coco["annotations"] = prediction
        prediction_coco["images"] = gt.dataset["images"]
        prediction_coco["categories"] = gt.dataset["categories"]

        # COCO object instantiation
        
        prediction = COCO()
        prediction.dataset = prediction_coco
        prediction.createIndex()

        self.ground_truth = gt
        self.prediction = prediction
        self.eval = COCOeval(gt, prediction, iouType='bbox')
        self.params = self.eval.params
        self._imgIds = gt.getImgIds()
        self._catIds = gt.getCatIds()
        # catname = [cat['name'] for cat in _coco.loadCats(_coco.getCatIds())]
        self.th = th
        if params:
            self.params = params
            self.eval.params = params
            self.eval.params.imgIds = sorted(self._imgIds)
            self.eval.params.catIds = sorted(self._catIds)

    def _build_no_cat_params(self):
        params = Params(iouType='bbox')
        params.maxDets = [500]
        params.areaRng = [[0 ** 2, 1e5 ** 2]]
        params.areaRngLbl = ['all']
        params.useCats = 0
        params.iouThrs = [self.th]
        return params

    def build_confussion_matrix(self, 
        out_image_filename=None,
        out_csv_filename=None):
        
        params = self._build_no_cat_params()
        self.eval.params = params
        self.eval.params.imgIds = sorted(self._imgIds)
        self.eval.params.catIds = sorted(self._catIds)
        self.eval.evaluate()

        ann_true = []
        ann_pred = []

        for evalImg, ((k, _), ious) in zip(self.eval.evalImgs, self.eval.ious.items()):
            ann_true += evalImg['gtIds']
            if len(ious) > 0:
                valid_ious = (ious >= self.th) * ious
                matches = valid_ious.argmax(0)
                matches[valid_ious.max(0) == 0] = -1
                ann_pred += [evalImg['dtIds'][match] if match > -1 else -1 for match in matches]
            else:
                ann_pred += ([-1] * len(evalImg['gtIds']))
            
        y_true = [ann['category_id'] for ann in self.ground_truth.loadAnns(ann_true)]
        y_pred = [-1 if ann == -1 else self.prediction.loadAnns(ann)[0]['category_id'] for ann in ann_pred]
        y_true = [y + 1 for y in y_true]
        y_pred = [y + 1 for y in y_pred]
                
        cats = ['background'] + [cat['name'] for _, cat in self.ground_truth.cats.items()]
        cnf_mtx = confusion_matrix(y_true, y_pred, normalize='true')
                  
        cnf_mtx_display = ConfusionMatrixDisplay(confusion_matrix=cnf_mtx, 
            display_labels=cats)
        
        _, ax = plt.subplots(figsize=(10, 9))
        plt.rcParams.update({'font.size': 11})
        cnf_mtx_display.plot(ax=ax, values_format='.3f',xticks_rotation=45, cmap="cividis")
        if out_image_filename is not None:
            cnf_mtx_display.figure_.savefig(out_image_filename, bbox_inches='tight')

        cls_report = classification_report(y_true, y_pred, 
            target_names=cats,output_dict=True,
            zero_division=1)

        ####format classification report
        cls_report_format = []
        no_print = ['background', 'macro avg', 'weighted avg', 'accuracy']
        cls_report_format.append(['class','precision','recall','f1-score'])
        for key, val in cls_report.items():
            if key not in no_print:
                cls_report_format.append([f'{key}',
                    str(round(val["precision"],2)),
                    str(round(val["recall"],2)),
                    str(round(val["f1-score"],2))
                ])
            if key == 'accuracy':
                cls_report_format.append([f'{key}',
                    round(val,2),
                    '',
                    ''
                ])

        return cls_report_format
        pass

    def run_coco_metrics(self, ap_type='all', 
        coco_iou= 0.95,
        areasize=32,
        out_csv_filename=None):

        summary_all = []
        self.eval.params = self.params
        self.eval.params.imgIds = sorted(self._imgIds)
        self.eval.params.catIds = sorted(self._catIds)
        self.eval.evaluate()
        self.eval.accumulate()
        print(f'\n|____Overall')
        self.eval.summarize()
        
        f = io.StringIO()
        with redirect_stdout(f):
            print(f'|____Overall')
            self.eval.summarize()
            
        out = f.getvalue()
        summary_all.append(out)
        out = out.split('\n')
        if ap_type == 'all':
            map_95 = out[0].split('=')[-1]
            map_50 = out[1].split('=')[-1]
            map_75 = out[2].split('=')[-1]

        if ap_type == 'objarea':
            if areasize == 20:
                map_tiny = out[3].split('=')[-1]    
            else:
                map_small = out[3].split('=')[-1]
            map_med = out[4].split('=')[-1]
            map_large = out[5].split('=')[-1]

        cat_name = [cat['name'] for _, cat in self.ground_truth.cats.items()]
        
        print('\n\n|__Class-wise coco evaluation')
        for c_id in self._catIds:
            print(f'\n|____Category: {c_id} : {cat_name[c_id-1]}')
            ff = io.StringIO()
            with redirect_stdout(ff):
                self.eval.params.catIds = [c_id]
                self.eval.evaluate()
                self.eval.accumulate()
            
            self.eval.summarize()
            f = io.StringIO()
            with redirect_stdout(f):
                print(f'\n|____Category: {c_id} : {cat_name[c_id-1]}')
                self.eval.summarize()
            out = f.getvalue()
            summary_all.append(out)
        return summary_all

################################################################################  
def build_params(coco_iou, areasize):
    
    params = Params(iouType='bbox')

    if coco_iou == 0.5 or coco_iou == 0.75:
        params.iouThrs = np.array([coco_iou]) 
    params.maxDets = [1, 10, 100]
    # params.areaRng = [[0 ** 2, 1e5 ** 2], [0 ** 2, 32 ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]
    params.areaRng = [[0 ** 2, 1e5 ** 2], [0 ** 2, areasize ** 2], [32 ** 2, 96 ** 2], [96 ** 2, 1e5 ** 2]]
    params.areaRngLbl = ['all', 'small', 'medium', 'large']
    params.useCats = 1
    return params

################################################################################
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gtfile", 
        type=str, 
        help="ground truth [in coco format] json file path")
    parser.add_argument("--predfile", 
        type=str, 
        help="prediction [in coco format] json file path")
    parser.add_argument("--statpath", 
        type=str, 
        default='./statistics',
        help="output directory path to save stats file")
    parser.add_argument("--conf_iou", 
        type=float,
        default=0.5, 
        help="confusion matrix iou threahold")
    args = parser.parse_args()

    if (args.gtfile is None) or (args.predfile is None):
        print('gt/prediction file missing!')
        exit()

    os.makedirs(args.statpath, exist_ok = True)
    args.confmat = f'{args.statpath}/bbox.png'
    args.outcsv = f'{args.statpath}/bbox.result.log'
  
    ap = 'all'
    coco_iou = 0.95 #set to 0.95 for default coco evaluation
    areasize = 32 #set to 32 for default coco evaluation
    params = build_params(coco_iou, areasize)  # Params for COCO metrics
    performance_evaluation = DetectionPerformanceEvaluation(args.gtfile, args.predfile, params=params,
                                                            th=args.conf_iou)
    cls_report = performance_evaluation.build_confussion_matrix(args.confmat, args.outcsv)
    summary_all = performance_evaluation.run_coco_metrics(ap, coco_iou, areasize, args.outcsv)
    csv_write(args.outcsv,
              summary_all)

    print('\n[done]\n')
################################################################################

if __name__ == '__main__':
    main()
