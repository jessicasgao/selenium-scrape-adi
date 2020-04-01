from utils.adi_downloader import load_config, download_adi

if __name__ == "__main__":
    config = load_config("config.json")

    download_adi(config["download_dir"],
                 config["download_subfolder_dir"],
                 config["output_dir"],
                 config["password"],
                 config["username"])