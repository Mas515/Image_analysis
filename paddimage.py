#create a cellprofiler module that adds padding to an image

import cellprofiler_core.module as cpm
import cellprofiler_core.setting as cps
import cellprofiler_core.image as cpi
import cellprofiler_core.measurement as cpmeas
import numpy as np
import skimage.transform as skt

class PadImage2(cpm.Module):
    module_name = "PadImage2"
    variable_revision_number = 1
    category = "Image Processing"
    
    def create_settings(self):
        self.input_image_name = cps.ImageNameSubscriber(
            "Input image name", cps.NONE, doc="Select the image to be padded"
        )
        self.output_image_name = cps.ImageNameProvider(
            "Output image name", "PaddedImage", doc="Select the name for the padded image"
        )
        self.padding = cps.Integer(
            "Padding", 10, doc="Select the amount of padding to add to the image"
        )
    
    def settings(self):
        return [self.input_image_name, self.output_image_name, self.padding]
    
    def visible_settings(self):
        return [self.input_image_name, self.output_image_name, self.padding]
    
    def run(self, workspace):
        input_image_name = self.input_image_name.value
        output_image_name = self.output_image_name.value
        padding = self.padding.value
        
        input_image = workspace.image_set.get_image(input_image_name)
        input_pixels = input_image.pixel_data
        output_pixels = np.pad(input_pixels, padding, mode="constant")
        
        output_image = cpi.Image(output_pixels, parent_image=input_image)
        workspace.image_set.add(output_image_name, output_image)
        
        if self.show_window:
            workspace.display_data.input_pixels = input_pixels
            workspace.display_data.output_pixels = output_pixels
    
    def display(self, workspace, figure):
        figure.set_subplots((1, 2))
        
        figure.subplot_imshow_grayscale(
            0, 0, workspace.display_data.input_pixels, "Input image"
        )
        figure.subplot_imshow_grayscale(
            0, 1, workspace.display_data.output_pixels, "Output image"
        )
