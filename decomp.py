import gedcom as gdcm
import sys

PathDicom = "./echo_data/"
file1 = PathDicom+'80692531.dcm'
file2 = PathDicom+'80692531dcomp.dcm'

r = gdcm.ImageReader()
r.SetFileName( file1 )
if not r.Read():
    sys.exit(1)

image = gdcm.Image()
ir = r.GetImage()

  image.SetNumberOfDimensions( ir.GetNumberOfDimensions() );
  dims = ir.GetDimensions();
  print ir.GetDimension(0);
  print ir.GetDimension(1);
  print "Dims:",dims

  #  Just for fun:
  dircos =  ir.GetDirectionCosines()
  t = gdcm.Orientation.GetType(dircos)
  l = gdcm.Orientation.GetLabel(t)
  print "Orientation label:",

  image.SetDimension(0, ir.GetDimension(0) );
  image.SetDimension(1, ir.GetDimension(1) );

  pixeltype = ir.GetPixelFormat();
  image.SetPixelFormat( pixeltype );

  pi = ir.GetPhotometricInterpretation();
  image.SetPhotometricInterpretation( pi );

  pixeldata = gdcm.DataElement( gdcm.Tag(0x7fe0,0x0010) )
  str1 = ir.GetBuffer()
  #print ir.GetBufferLength()
  pixeldata.SetByteValue( str1, gdcm.VL( len(str1) ) )
  image.SetDataElement( pixeldata )

  w = gdcm.ImageWriter()
  w.SetFileName( file2 )
  w.SetFile( r.GetFile() )
  w.SetImage( image )
  if not w.Write():
    sys.exit(1)
Generated on Mon Jul 29 2013 11:24:11 for GDCM by doxygen 1.7.1
SourceForge.net Logo
