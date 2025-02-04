from PIL import Image

def apply_mean_filter(image,kernel_size):
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
            #Summing pixels in the kernel
            sum_r = sum_g = sum_b = 0
            for ki in range(-k_half,k_half+1):
                for kj in range(-k_half,k_half+1):
                    r,g,b = pixels[i+ki,j+kj]
                    sum_r +=r
                    sum_g +=g
                    sum_b += b
                    
            #average the sum
            num_pixels = kernel_size * kernel_size
            output_pixels[i,j] = (sum_r // num_pixels, sum_g // num_pixels, sum_b // num_pixels)
            
# Handle the edges (optional, could also be left unprocessed)
# Copy edge pixels from the original image or implement a different strategy
    return output_image

image_path = "orginal1.png"
original_image = Image.open(image_path)
kernel_size = 5 #define kernel size, must be an odd number
filtered_image = apply_mean_filter(original_image, kernel_size)
filtered_image.show()
