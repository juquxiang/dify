# from PIL import Image, ImageDraw

# def crop_circle(image_path, output_path):
#     """裁剪图片为圆形"""
#     img = Image.open(image_path).convert("RGBA")
#     size = img.size
#     mask = Image.new("L", size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
#     result = Image.new("RGBA", size, (0, 0, 0, 0))
#     result.paste(img, mask=mask)
#     result.save(output_path, "PNG")

# def crop_rounded_rectangle(image_path, output_path, radius=20):
#     """裁剪图片为圆角矩形"""
#     img = Image.open(image_path).convert("RGBA")
#     size = img.size
#     mask = Image.new("L", size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    
#     result = Image.new("RGBA", size, (0, 0, 0, 0))
#     result.paste(img, mask=mask)
#     result.save(output_path, "PNG")

# # 示例使用
# crop_circle("logo1.png", "circle_output.png")
# crop_rounded_rectangle("logo1.png", "rounded_output.png", radius=200)
from PIL import Image, ImageDraw

def png_to_ico_circle(input_png, output_ico, size=(256, 256)):
    # 打开 PNG 图片
    img = Image.open(input_png).convert("RGBA")
    img = img.resize(size, Image.LANCZOS )
    
    # 创建一个相同大小的透明图像
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    
    # 画一个白色的圆形遮罩
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
    # 把原图和遮罩结合
    img.putalpha(mask)
    
    # 保存为 ICO 文件
    img.save(output_ico, format="ICO")

# 使用示例
png_to_ico_circle("logo.png", "logo.ico")