import os
import lasio

def single_convert(input_file, output_file):
    l = lasio.read(input_file)    
    k = 0.3048
    l_dt = l["DT"] # muS/ft
    l_dt_muSm = l_dt / 0.3048;
    l.add_curve("DTm", l_dt_muSm)
    with open(output_file, mode='w') as f:
        l.write(f)
        
def batch_convert(data_path, filenames):
    input_files = [ (lambda x: os.path.join(data_path, x))(f) for f in filenames ]
    for input_file in input_files:
        filename_root, ext = os.path.splitext(os.path.basename(input_file))
        output_file = os.path.join(data_path, filename_root + '-m.las')
        single_convert(input_file, output_file)
        
if __name__ == "__main__":
    data_path = 'D:\\Data\\PAYS\\project12\\Logs\\'
    filenames = ['F-O1.las', 'F-O2.las', 'F-O3.las', 'F-O4.las']
    batch_convert(data_path, filenames)