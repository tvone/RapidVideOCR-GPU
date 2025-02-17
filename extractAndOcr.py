from rapid_videocr import RapidVideoSubFinderOCR

vsf_exe = r"C:\Users\Cuong\Desktop\rapidOCR\VideoSubFinder_6.10_x64\VideoSubFinderWXW"
extractor = RapidVideoSubFinderOCR(vsf_exe_path=vsf_exe, is_concat_rec=True)

# video_path can be directory path or video full path.
video_path = 'D:\\A-aman_0839\\apa.mp4'
save_dir = 'outputs'
extractor(video_path, save_dir)

