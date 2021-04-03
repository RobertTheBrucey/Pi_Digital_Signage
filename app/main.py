import configparser as cp
import os
import ffmpeg

if __name__ == "__main__":
    #Check for config file, else create it
    config = cp.ConfigParser()
    if os.path.exists("config.ini"):
        config.read("config.ini")
    else:
        #Define and save default config here
        config['APP'] = {'MediaDirectory': 'media',
                         'MediaConfig': 'media.ini',
                         'Mode': 'auto'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    #Create media folder if it doesn't exist
    if not os.path.exists(config['APP']['MediaDirectory']):
        try:
            os.mkdir(config['APP']['MediaDirectory'])
        except OSError:
            print(f"Failed to create {config['APP']['MediaDirectory']} dirrectory")
        else:
            print(f"Directory {config['APP']['MediaDirectory']} successfully created")
    
    #Check for media config, otherwise create
    media_conf = cp.ConfigParser()
    if os.path.exists(config['APP']['MediaConfig']):
        media_conf.read(config['APP']['MediaConfig'])
    else:
        videos = []
        images = []
        mime = magic.Magic(mime.True)
        for (path, path_names, file_names) in os.walk(config['APP']['MediaConfig']):
            for name in file_names:
                full_path = os.path.join(path, name)
                try:
                    probe = ffmpeg.probe(full_path)
                except ffmpeg.Error:
                    pass
                if 'Video' in probe:
                    if 'Duration: N/A' in probe:
                        images.append(full_path)
                    else:
                        videos.append(full_path)