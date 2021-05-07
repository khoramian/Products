from updater4pyi import upd_source, upd_core

swu_source = upd_source.UpdateGithubReleasesSource('khoramian/Reverse_TCP_Shell')
swu_updater = upd_core.Updater(current_version=0.1,
                               update_source=swu_source)

if __name__ == '__main__':
    print("hiiiiiiiiiiiiiiiiiiiiiiiiii")