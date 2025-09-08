# Analise de Video com Python / Video Analysis with Python
## This project uses Python and OpenCV to make possible to analize video's quality
It takes four steps to come up with the outcome:

- Resolution
- Luminosity
- Blur
- Video Shake

## Resolution
  As it is said, the resolution part will show the resolution of the video, e.g. 1900x1820 pixels. It is measured in pixels.

## Luminosity
  In the Luminosity part, it will analize each pixel of each frame and change the colours to Grayscale so it can return values in the interval between 0 and 255. Then, it arranges it into an array containing all these values and, at the end, it returns the mean and median of the luminosity. 
  The mean is for understanding what is the average value that shows up in each frame, on the other hand, the median is used as a robust method, so it can handle outliers properly. If the outcome is closer to 0 the video is darker, if not, it is brighter.

## Blur
  This is the most complex part, because it requires to understand Calculus and the use of the Laplacian to deeply understand the concept used. However, as we cannot have a calculus course to simply understand this code, I will briefly explain this in a simple way.
  - First, it will look the amount of details of the frame(edges, lines, textures).
  - If the pixels change a lot from one spot to another the image is sharp. If they change a little, the image is blurry.
  - And, finally, the results: It will also return the mean and the median for reasons previously mentioned. The higher the result is cleaner/sharpest is the video. 

## Video Shake
  This part is responsible to verify if the video is whether stable or not. It works as it follows:
  - First, it will see the rate of change of the pixels from each frame to the other.
  - If it changes a lot from one frame to the other, the video is shaken. If not, it is stable.
  - The result is a float number, e.g 3.00 or 5.12
  It is problable that the range of the results are not that big, so it means the results will not pass a value of 10.00. Actually, it will not even reach it.
  When trying by yourselves, it is a good practice to evaluate the result and create your own scale to see if it fits to your sample.

## Results
After all these steps, it will return a CSV file containing these following labels:
- width
- length
- media_luminosidade = luminosity mean
- mediana_luminosidade = luminosity median
- media_blur = blur mean
- mediana_blur = blur median
- tremor = video shake
- tempo_segundos = time in seconds for analizing one video

Feel free to edit and improve this repository.

-----------------------------------------------------------------------------------

## License

MIT License

Copyright (c) 2025 Pedro Galvani Bertasso

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


