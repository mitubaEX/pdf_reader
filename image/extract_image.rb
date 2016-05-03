# coding: utf-8
require 'origami'

include Origami

pdf = PDF.read(ARGV[0])

images = pdf.root_objects.find_all {|obj| obj.is_a?(Graphics::ImageXObject)}
count = 0
images.each do |stream|
  ext, image_data = stream.to_image_file
  count += 1
  image_file = "#{count}.#{ext}"
  File.open(image_file, "wb") do |f|
   f.write(image_data)
  end
end
