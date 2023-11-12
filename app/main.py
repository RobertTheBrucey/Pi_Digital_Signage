import configparser as cp
import os
import ffmpeg
platform = 'cat /proc/cpuinfo'
#https://ozzmaker.com/check-raspberry-software-hardware-version-command-line/

if __name__ == "__main__":
    print("Starting ART Pi Py")
    #Check for config file, else create it
    config = cp.ConfigParser()
    if os.path.exists("config.ini"):
        config.read("config.ini")
        print("Configuration found and loaded")
    else:
        print("No Configuration file found, generating")
        #Define and save default config here
        config['APP'] = {'MediaDirectory': 'media',
                         'MediaConfig': 'media.ini',
                         'Mode': 'auto',
                         'RescanMediaOnLaunch': False
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print("Configuration file generated")

    #Create media folder if it doesn't exist
    if not os.path.exists(config['APP']['MediaDirectory']):
        print("Media directory not found, creating")
        try:
            os.mkdir(config['APP']['MediaDirectory'])
        except OSError:
            print(f"Failed to create {config['APP']['MediaDirectory']} dirrectory")
        else:
            print(f"Directory {config['APP']['MediaDirectory']} successfully created")
    
    #Check for media config, otherwise create
    media_conf = cp.ConfigParser()
    if os.path.exists(config['APP']['MediaConfig']):
        print("Loading Media configuration")
        media_conf.read(config['APP']['MediaConfig'])
        print("Media configuration loaded")
    else:
        config['APP']['RescanMediaOnLaunch'] = True 
        print("No Media configuration found, generating")
        media_conf['Video'] = {'Volume': 100,
                               'AudioEnabled': True,
                               'Subtitles': False,
                               'Autorotate': True
        }
    if config['APP']['RescanMediaOnLaunch']:
        print("Scanning for new media. To disable edit config.ini")
        videos = []
        images = []
        for (path, path_names, file_names) in os.walk(config['APP']['MediaConfig']):
            for name in file_names:
                full_path = os.path.join(path, name)
                try:
                    probe = ffmpeg.probe(full_path)
                except ffmpeg.Error:
                    pass
                if probe['streams'][0]['codec_type'] == 'video':
                    if 'duration_ts' in probe['streams'][0].keys():
                        videos.append(full_path)
                    else:
                        images.append(full_path)
        #Generate Media Config
            if not 'Mode' in media_conf.keys():
                media_conf['Mode'] = 'video' if len(videos) > 0 else 'image'
            media_conf['Video']['Videos'] = videos
            media_conf['Image']['Images'] = images
    
    #Transcoding step