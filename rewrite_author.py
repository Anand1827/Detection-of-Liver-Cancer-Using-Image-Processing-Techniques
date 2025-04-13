def commit_callback(commit):
    if commit.author_name == b'Koushik Rdy':
        commit.author_name = b'Anand Busharaju'
    if commit.author_email == b'koushikrdyt@gmail.com':
        commit.author_email = b'bhusharajuanand2002@gmail.com'

    if commit.committer_name == b'Koushik Rdy':
        commit.committer_name = b'Anand Busharaju'
    if commit.committer_email == b'koushikrdyt@gmail.com':
        commit.committer_email = b'bhusharajuanand2002@gmail.com'
