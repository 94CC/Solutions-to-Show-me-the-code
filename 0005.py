import os,sys
from PIL import Image

def change_size(file,outdir):
    """
    file:the full path of the input file
    outdir:target directory of output file.
        """
    size=(1136,640)
    filename=os.path.basename(file)
    outfile=outdir+os.path.splitext(filename)[0]+'_thumbnail' #get rid of the file extension
    if file !=outfile:
        try:
            im=Image.open(file)
            im.thumbnail(size)
            im.save(outfile+'.JPEG')
        except Exception as e:
            print ('Errors occur at ',file)
            print (repr(e))
            
def process_files():
    for indir in sys.argv[1:]:
        indir=os.path.split(indir)[0] #get rid of the path seperator so that we can change the modify the directory name
        outdir=indir+'.thumbnail/'
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        for infile in os.listdir(indir):
            infile=indir+os.path.sep+infile
            change_size(infile,outdir)
            
#--------Program starts----------        
print ("""
---------------------
function:process photos in one or more directories by changing the size of photos to 
         not more than the resolution ratio of iphone 5s. save the new photos in a new directory.
operation:running python script in cmd. The second argument is the path of the directory
language:python 3.5
----------------------""")
if __name__=='__main__':
    process_files()