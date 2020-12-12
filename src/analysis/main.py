from analysis import Analysis
from draw import draw
import argparse
import numpy as np

DEBUG = True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-V',
                        '--videopath',
                        help='Path to the video file or directory',
                        dest='videopath',
                        required=False,
                        metavar='VIDEODIR')
    parser.add_argument('-H',
                        '--h5path',
                        help='Path to the h5 file',
                        dest='h5path',
                        required=False,
                        metavar='H5DIR')
    parser.add_argument('output_dir',
                        help='Output Directory of the json files',
                        nargs='?',
                        metavar='OUTDIR')
    args = parser.parse_args()

    if args.h5path is not None:
        h5path = args.h5path
    if args.videopath is not None:
        videopath = args.videopath
    if args.h5path is None and args.videopath is None:
        if DEBUG == True:
            print("Setting h5path and videopath to defaults in DEBUG")
            h5path = (r'C:\Users\Ma990\Code\spel\whisking\sample-project'
                   r'\Whisking_with_Midline-Frank Ma-2020-05-03\videos'
                   r'\iteration-2\6400ratDLC_resnet50_Whisking_with_Midline'
                   r'May3shuffle1_500000.h5')
            videopath = (r'C:\Users\Ma990\Code\spel\whisking\sample-project'
                     r'\Whisking_with_Midline-Frank Ma-2020-05-03\videos'
                     r'\iteration-2\6400ratDLC_resnet50_Whisking_with_Midline'
                     r'May3shuffle1_500000_labeled.mp4')
        else:
            raise RuntimeError("""You need to provide either a video directory 
                        or the DLC generated .h5 file.""")

    DLCscorer = 'DLC_resnet50_Whisking_with_MidlineMay3shuffle1_500000'
    
    analysis = Analysis(h5_path=h5path, 
                        DLCscorer=DLCscorer, 
                        startframe=0, 
                        endframe=5305)
    analysis.calc_whisker_angles(fill_gaps=False,
                                 fps=239.76)
    analysis.plot_whisker_angles()
    analysis.calc_blink_signal(fill_gaps=False,
                               fps=239.76)
    analysis.plot_blink_signal()
    analysis.savecsv()

    analysis.annotate_video(videopath=videopath)

if __name__ == '__main__':
    main()