# timeline25.github.io
Simply contain the latest PDFs for download, linked from the QR codes on the timelines itself.

# Repository for latest PDF versions of the timeline project

[![GitHub release](https://img.shields.io/github/release/timeline25/timeline25.github.io.svg)](https://GitHub.com/timeline25/timeline25.github.io/releases/)
[![MIT license](https://img.shields.io/github/license/timeline25/timeline25.github.io)](https://kreier.mit-license.org/)
[![pages-build-deployment](https://github.com/timeline25/timeline25.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/timeline25/timeline25.github.io/actions/workflows/pages/pages-build-deployment)

This website contains the latest PDFs for download, linked from the QR codes on the [timelines](https://github.com/kreier/timeline) itself.

![timeline 5.10](https://raw.githubusercontent.com/timeline25/timeline25.github.io/refs/heads/main/test/timeline20251007_v5.10.png)

| language                                                                |                   print                                     | version | last updated |
|-------------------------------------------------------------------------|:-----------------------------------------------------------:|:-------:|:------------:|
| [German (Deutsch)](https://timeline25.github.io/timeline_de.pdf)        | [link](https://timeline25.github.io/timeline_de_print.pdf)  |   5.10  |  2025-10-10  |
| [English](https://timeline25.github.io/timeline_en.pdf)                 | [link](https://timeline25.github.io/timeline_en_print.pdf)  |   5.10  |  2025-10-10  |
| [Vietnamese (Tiếng Việt)](https://timeline25.github.io/timeline_vi.pdf) | [link](https://timeline25.github.io/timeline_vi_print.pdf)  |   5.10  |  2025-10-10  |

The print version has additional 5cm left and right for the print shop. It's easier to connect the end roll covers to the timeline. The standard dimensions for the print version are 1308x210mm. But it can be scaled to any size with a ratio 6.228:1. 

## Project repository

The work on the timeline is done and documented at the repository [https://github.com/kreier/timeline](https://github.com/kreier/timeline).

The idea for this project started with spreadsheets in 2009. I moved to vector graphics in 2015. Then from 2023 on it was finally generated with a python program and the __reportlab package__ to make the creation, translation and editing much faster and easier. We stopped using reportlab with version 4.6 in summer 2024 and moved to [fpdf2](https://py-pdf.github.io/fpdf2/index.html) with 4.7 to support complicated glyph composition for languages like Khmer, Sinhala and Arabic that requires a specific shape engine like [harfbuzz](https://github.com/harfbuzz/harfbuzz).

## Improvement - report mistakes

If you spot a mistake, please add an issue at [https://github.com/kreier/timeline/issues](https://github.com/kreier/timeline/issues)

## Create your own PDF in a browser

To greate your own version just using a browser you can try out this [Jupyter Notebook at Google Colab](https://colab.research.google.com/drive/1G0z6jKIs_B_Md_y6Wen108Keo5WazalZ?usp=sharing). Simply press __Runtime - Run all__. It requires less than 60 seconds. Since June 2024 there is also [a version 4.7 with fpdf2](https://colab.research.google.com/drive/1WbLz2Gz775j0bSFPHdQihAkub3wltAof?usp=sharing) to support RTL scripts, Khmer and Sinhala.

- Jupyter notebook [in Google Colab with reportlab](https://colab.research.google.com/drive/1G0z6jKIs_B_Md_y6Wen108Keo5WazalZ?usp=sharing)
- Jupyter notebook [in Google Colab with fpdf2](https://colab.research.google.com/drive/1WbLz2Gz775j0bSFPHdQihAkub3wltAof?usp=sharing)

## Edit your own edition in a browser

To edit the files in the browser its best to have your own Github account. Fork the [timeline](https://github.com/kreier/timeline) repository and create a Codespace within the fork. Install the needed 3 libraries (reportlab, svglib and googletranslate) and the CSV extention to Visual Studio Code. You're good to go! Change everything you want - just using the browser.
