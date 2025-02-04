
from PIL import Image

def apply_median_filter(image,kernel_size):
    #load image and convert to RGB (in case its not)
    img = image.convert('RGB')
    pixels = img.load()
    
    #image dimensions 
    width,height = img.size
    
    #prepare output image
    output_image = Image.new('RGB', (width,height))
    output_pixels = output_image.load()
    
    #compute half-size of the kernel for boundary conditions
    k_half = kernel_size // 2

    #iterate over every pixel that can fully accomodate the kernel
    for i in range(k_half,width - k_half):
        for j in range(k_half, height - k_half):
            #collecting pixel values in the kernel
            channel_r = []
            channel_g = []
            channel_b = []
            for ki in range(-k_half, k_half+1):
                for kj in range(-k_half,k_half+1):
                    r, g, b = pixels[i+ki, j+kj]
                    channel_r.append(r)
                    channel_g.append(g)
                    channel_b.append(b)
                    
            #sorting and finding the median 
            channel_r.sort()
            channel_g.sort()
            channel_b.sort()
            median_r = channel_r[len(channel_r)//2]
            median_g = channel_g[len(channel_g)//2] 
            median_b = channel_b[len(channel_b)//2]                     
            output_pixels[i,j] = (median_r,median_g,median_b)
            
#Handle the edges (optional )
    return output_image

image_path = "orginal1.png"
original_image = Image.open(image_path)
kernel_size= 5
filtered_image = apply_median_filter(original_image, kernel_size)
filtered_image.show()            
