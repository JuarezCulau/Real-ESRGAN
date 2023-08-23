# Usage: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile -o outfile [options]...
#
# A common command: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile --outscale 3.5 --face_enhance
#

#   -h                   show this help
#   -i --input           Input image or folder. Default: inputs
#   -o --output          Output folder. Default: results
#   -n --model_name      Model name. Default: RealESRGAN_x4plus
#   -s, --outscale       The final upsampling scale of the image. Default: 4
#   --suffix             Suffix of the restored image. Default: out
#   -t, --tile           Tile size, 0 for no tile during testing. Default: 0
#   --face_enhance       Whether to use GFPGAN to enhance face. Default: False
#   --fp32               Use fp32 precision during inference. Default: fp16 (half precision).
#   --ext                Image extension. Options: auto | jpg | png, auto means using the same extension as inputs. Default: auto

infile = "C:/Users/juare/Documents/GitHub/Real-ESRGAN/inputs"

python inference_realesrgan.py -n RealESRGAN_x4plus -i C:/Users/juare/Documents/GitHub/Real-ESRGAN/inputs --face_enhance -g 0

python inference_realesrgan.py -n RealESRGAN_x4plus -i C:/Users/juare/Documents/GitHub/Real-ESRGAN/inputs -o C:/Users/juare/Documents/GitHub/Real-ESRGAN/testoutput --outscale 4 --face_enhance True