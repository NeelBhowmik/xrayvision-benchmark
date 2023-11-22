# XVision Benchmark: Benchmarking of X-ray security imaging datasets

<!-- <p align="center">
  <img src="images/xray-history.png" />
</p> -->

*[List of datasets and papers (not exhaustive)]*

## Dataset

|Name       | Type | Year | Class |Prohibited - Negative| Annotations| Views|Open Source | 
|-----------|------|------|-------------|-------------|------|-----|------|
|FSOD       |2D    | 2022 |20            |12,333 - 0 | bbox|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/DIG-Beihang/XrayDetection)  |
|EDS       |2D    | 2022 |10            |14,219 - 0 | bbox|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/DIG-Beihang/XrayDetection)  |
|Xray-PI       |2D    | 2022 |12            |2,409 - 0 | bbox, mask|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/LPAIS/Xray-PI)  |
|PIXray       |2D    | 2022 |12            |5,046 - 0 | bbox, mask|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/Mbwslib/DDoAS)  |
|CLCXray       |2D    | 2022 |12            |9,565 - 0 | bbox|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/GreysonPhoenix/CLCXray)  |
|HiXray       |2D    | 2021 |8            |45,364 - 0 | bbox|1     |<span style="color:green;">✓</span> [[Link]](https://github.com/DIG-Beihang/XrayDetection)  |
|deei6       |2D    | 2021 |6            |7,022 - 0 | bbox, mask|2     |<span style="color:red;">✕</span> [[Link]](https://breckon.org/toby/publications/papers/bhowmik21energy.pdf)  |
|PIDray    |2D    | 2021 |12           |47,677 - 0  | bbox, mask |1     |<span style="color:green;">✓</span> [[Link]](https://github.com/bywang2018/security-dataset)       |
|AB       |2D    | 2021 |--            |417 - 6,608 | -- |2     |<span style="color:red;">✕</span> [[Link]](https://ieeexplore.ieee.org/document/9534034)  |
|dbf4       |2D    | 2020 |4            |10,112 - 0 | bbox, mask |4     |<span style="color:red;">✕</span> [[Link]](https://breckon.org/toby/publications/papers/isaac20multiview.pdf)  |
|OPIXray    |2D    | 2020 |5            |8,885  - 0 | bbox |1     |<span style="color:green;">✓</span>  [[Link]](https://github.com/OPIXray-author/OPIXray)           |
|SIXray     |2D    | 2019 |6            |8,929 - 1,050,0302 | bbox |1 |<span style="color:green;">✓</span> [[Link]](https://github.com/MeioJane/SIXray)           |
|COMPASS-XP     |2D    | 2019 |366            |1928 - 0 | -- |1 |<span style="color:green;">✓</span> [[Link]](https://zenodo.org/record/2654887#.YUtGVHVKikA)           |
|dbf6       |2D    | 2018 |6            |11,627 - 0 | bbox, mask |4    |<span style="color:red;">✕</span> [[Link]](https://breckon.org/toby/publications/papers/akcay18architectures.pdf)  |
|GDXray       |2D    | 2015 |5            |19,407 - 0 | bbox |1     |<span style="color:green;">✓</span> [[Link]](https://domingomery.ing.puc.cl/material/gdxray/)  |
|Dur_3D       |3D    | 2020 |5            |774 - 0 | bbox | --   |<span style="color:red;">✕</span> [[Link]](https://arxiv.org/abs/2008.01218)  |
|Flitton_3D       |3D    | 2015 |2        |810 - 2149 | bbox | --   |<span style="color:red;">✕</span> [[Link]](https://breckon.org/toby/publications/papers/flitton15codebooks.pdf)  |

---

## OPIXray

| Model      | Folding | Straight | Scissor | Utility | M-tool | mAP   |
|------------|---------|----------|---------|---------|--------|-------|
| CR-CNN     | 0.934   | 0.771    | 0.961   | 0.836   | 0.949  | 0.890 |
| FSAF       | 0.821   | 0.804    | 0.956   | 0.805   | 0.868  | 0.851 |
| DDETR      | 0.909   | 0.774    | 0.963   | 0.859   | 0.934  | 0.888 |
| FRCNNw/ST  | 0.945   | 0.842    | 0.977   | 0.854   | 0.959  | 0.915 |
| YOLOX      | 0.908   | 0.801    | 0.974   | 0.859   | 0.935  | 0.896 |
| CenterNet  | 0.911   | 0.758    | 0.977   | 0.820   | 0.909  | 0.875 |


## SIXray10

| Model      | Firearm | Knife | Wrench | Pliers | Scissors | mAP   |
|------------|---------|-------|--------|--------|----------|-------|
| CR-CNN     | 0.882   | 0.824 | 0.838  | 0.882  | 0.873    | 0.860 |
| FSAF       | 0.894   | 0.776 | 0.792  | 0.885  | 0.898    | 0.849 |
| DDETR      | 0.913   | 0.934 | 0.910  | 0.944  | 0.960    | 0.932 |
| FRCNNw/ST  | 0.897   | 0.856 | 0.899  | 0.920  | 0.947    | 0.904 |
| YOLOX      | 0.909   | 0.869 | 0.891  | 0.907  | 0.938    | 0.903 |
| CenterNet  | 0.906   | 0.862 | 0.887  | 0.918  | 0.908    | 0.896 |


## PIDray

| Model      | Baton                  | Pliers                 | Hammer                 | Powerbank              | Scissors               | Wrench                 | Gun                    | Bullet                 | Sprayer                | HandCuffs              | Knife                  | Lighter                | mAP                   |
|------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|
| CR-CNN     | .985/.933/.357       | .999/.965/.916       | .960/.898/.774       | .953/.951/.753       | .958/.926/.735       | .984/.969/.930       | .158/.416/.655       | .945/.873/.332       | .775/.892/.544       | .989/.983/.989       | .379/.630/.479       | .843/.741/.125       | .827/.848/.633       |
| FSAF       | .982/.940/.357       | .999/.970/.890       | .965/.906/.719       | .952/.965/.672       | .924/.931/.621       | .979/.957/.942       | .088/.307/.550       | .950/.909/.264       | .748/.866/.595       | .988/.982/.990       | .279/.615/.474       | .855/.765/.114       | .809/.843/.599       |
| DDETR      | .989/.952/.589       | .999/.983/.941       | .971/.945/.860       | .969/.968/.723       | .970/.968/.845       | .987/.983/.981       | .099/.337/.645       | .966/.877/.384       | .950/.914/.703       | .988/.986/.990       | .578/.724/.537       | .872/.781/.388       | .861/.868/.716       |
| FRCNNw/ST  | .988/.976/.717       | .990/.979/.949       | .988/.952/.921       | .969/.978/.835       | .981/.963/.910       | .988/.987/.990       | .506/.579/.756       | .962/.872/.505       | .958/.943/.676       | .988/.986/.990       | .692/.753/.620       | .867/.787/.906       | .906/.896/.765       |
| YOLOX      | .986/.958/.615       | .989/.986/.883       | .969/.943/.826       | .964/.966/.737       | .982/.964/.840       | .958/.987/.978       | .334/.472/.666       | .960/.902/.393       | .905/.928/.676       | .989/.986/.990       | .670/.707/.525       | .846/.795/.213       | .879/.883/.695       |
| CenterNet  | .977/.935/.935       | .990/.975/.914       | .972/.908/.655       | .952/.955/.649       | .967/.933/.649       | .983/.970/.963       | .278/.441/.568       | .891/.748/.207       | .732/.863/.334       | .989/.987/.989       | .439/.605/.362       | .851/.723/.143       | .835/.837/.566       |


## HiXray


## CLCXray


## PIXray


## GDXray


## deei6


## dbf6 


# :frog: Reference
If you use this repo and like it, use this to cite it:
```tex
@misc{xvision-benchmark,
      title={XVision Benchmark: Benchmarking of X-ray security imaging datasets},
      author={Neelanjan Bhowmik},
      year={2023},
      url={https://github.com/NeelBhowmik/xvision-benchmark}
    }