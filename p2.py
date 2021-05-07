from updater4pyi import upd_source, upd_core

swu_source = upd_source.UpdateGithubReleasesSource('khoramian/Products')
swu_updater = upd_core.Updater(current_version=...,
                               update_source=swu_source)

if __name__ == '__main__':
    print("hiiiiiiiiiiiiiiiiiiiiiiiiii")