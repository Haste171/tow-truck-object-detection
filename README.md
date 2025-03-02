<p align="center">
<br><br><br>
<a href="https://github.com/Haste171/tow-truck-object-detection">
    <img src="preview/preview.png" width="760px" height="400px">
    </a>
<br><br><br>
</p>



<p align="center">
<b> Object detection tools to detect tow trucks</b>
</p>

<p align=center>
<a href="https://universe.roboflow.com/david-xtmfo/tow-truck-object-detection"><img src="https://img.shields.io/badge/View_on-Roboflow-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAAAAXNSR0IArs4c6QAAAcZJREFUOE%2FNU79PGlEU%2Fvfnzpx5zodnZnZ3u5QmCQkhCBEYlypVwQUlhRWgihBQIFhVCP6BlFoRQu9JChFBVEUoIjBFFiU2lJjJY3cxMzszsv9%2B873pZ02%2Bvvt%2FnvN%2FPOc73vM4fOmiD5%2F4PN6cCCg%2Fd8WcUcfD6Wx8%2FDCEQUxaJDbkHs9FEBDsC3YQw3WawtMAqz2C2DlHfTml1S7SNRd2u7Ev13YaQuJHbAWwDNoxImNWBN9C17gR1OX%2F02OXf%2FoOEvUdhP4L0t4yo%2F5DMi64G7%2BR5Sm9w6cvVFLNVvce65eBOnw7toDRwbv%2Bq6aX96y4NFJveA3axgGXY7FRKnUN%2B78KxYIcdkj9u69tuHtnORmOjVx0PvwNuJq4jLgUBpnNPBvT48WYr%2BjoP0sPgDRflSkVRoh1A9NAXYb77Vp%2BC2bVX69f9xdNZVzidJ3poytMPVVp09Ivn%2Fpg3JDgfPqG49%2FjlNxbN2%2FdutpO8T4M3Ym9g%2Bbp5D5GrmHsf7lE%2BZBz%2FlEAAIo6z1hjeTIDccdi1ae8I4SzN0I4Z2%2Bh7FRCSau4FDTOW2g1btiCyvcPfLb6BEWWZfhav2Ns8rNPOxUR7Dt2j2vY7Lo0iCrvsTp74ngArvN%2Fj%2BGpmJMBQAAAABJRU5ErkJggg%3D%3D">
<a href="https://gitHub.com/Haste171/langchain-chatbot/graphs/commit-activity"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg">
<a href="https://github.com/Haste171/tow-truck-object-detection/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Haste171/tow-truck-object-detection">
<a href="https://discord.gg/KgmN4FPxxT"><img src="https://dcbadge.vercel.app/api/server/KgmN4FPxxT?compact=true&style=flat"></a>

</a>


## User-Setup
Join the [Discord](https://discord.gg/KgmN4FPxxT) server for help

## Dev-Setup
Prerequisites:
- [Git](https://git-scm.com/downloads) - Free

### Setup
```
git clone https://github.com/Haste171/tow-truck-object-detection.git
```

### Install Requirements

```python
poetry install
```

### Activate Environment
```python
poetry shell
```

### Setup ClearML for Logging
```python
clearml-init
```

### Access ClearML

Go to https://app.clear.ml/projects to access the project created once training starts to view logs etc.

# Usage

## Training
```python
python main.py train --dataset /path/to/dataset --model_size medium --name TowTruckModel --clear_ml_name TowTruckObjectDetection --patience 10
```

## Inference
```python
python main.py infer --image /path/to/image.jpg
```