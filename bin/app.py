import web
from MarkovRap import testMarkov

urls = (
    '/russesang', 'index'
)

 
app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(startword="")
        lyric = testMarkov(form.startword)
        return render.index(lyric = lyric)

if __name__ == "__main__":
    app.run()
