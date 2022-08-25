import matplotlib.pyplot as plt

# This code was given to us last year by Recep can, research assistant in the photogrammetry course I took last year. 
# I used this code to get the pixel points where I clicked in the images in txt format.

def get_pixel_coordinates_from_click(imagePath, outputfilename):

    im = plt.imread(imagePath)
    ax = plt.gca()
    fig = plt.gcf()
    implot = ax.imshow(im)
    filepath = outputfilename + ".txt"
    def onclick(event,filepath=filepath):
        if event.xdata != None and event.ydata != None:
            with open(filepath, "a") as text_file:
                print("{}\t{}".format(event.xdata, event.ydata),file=text_file)
  
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()


if __name__ == "__main__":
    image_path_1 = "florence2.jpg"
    measured_coordinates_1 = "coordinates_of_second_image_points" 
# try in order (for example first runing the get_pixel_coordinates_from_click(image_path_1, measured_coordinates_1) 
# after runing the get_pixel_coordinates_from_click(image_path_2, measured_coordinates_2) )

    get_pixel_coordinates_from_click(image_path_1, measured_coordinates_1)

