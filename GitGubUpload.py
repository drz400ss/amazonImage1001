import git

repo = git.Repo(local_dir)

# main ブランチがなければ作成
if "main" not in repo.heads:
    repo.git.checkout('-b', 'main')
else:
    repo.heads.main.checkout()

# すべてのファイルをステージング
repo.git.add(all=True)
repo.index.commit("Add AI white background images")

# リモート登録
if "origin" not in [r.name for r in repo.remotes]:
    origin = repo.create_remote('origin', 'https://<USERNAME>:<TOKEN>@github.com/drz400ss/amazon_images.git')
else:
    origin = repo.remotes.origin

# push
origin.push(refspec='main:main')
