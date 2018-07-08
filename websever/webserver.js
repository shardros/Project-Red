var http = require('http');
var fs = require('fs');
var formidable = require('formidable');
var cmd = require('node-cmd');
var io = require('socket.io')(http);

// html file containing upload form
var upload_html = fs.readFileSync("upload_file.html");
var playing_html = fs.readFileSync("playing.html");

// replace this with the location to save uploaded files
var upload_path = "/home/pi/red/websever/music/";


io.on('connection', function(socket){
    socket.on('stop', function(msg){
        console.log('STOP!!!!!!!!!!!!!!')
    });
});

http.createServer(function (req, res) {
    console.log('Got connection!');
    if (req.url == '/uploadform') {
        res.writeHead(200);
        res.write(upload_html);
        return res.end();
        var command = 'sudo python ../../lightshowpi/py/synchronized_lights.py --file=250m-silence.mp3';
        cmd.run(command);
    } else if (req.url == '/fileupload') {
        res.writeHead(200);
        res.write(playing_html);
        res.end();
        var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            // oldpath : temporary folder to which file is saved to
            var oldpath = files.filetoupload.path;
            var newpath = upload_path + files.filetoupload.name.replace(/\s/g, '');
            if (newpath.slice(-4) != '.mp3') {
                //Change the file name to something the computer gets
                newpath += '.mp3';
            }
            ;
            //Change the file name to something the computer gets
            // copy the file to a new location
            fs.rename(oldpath, newpath, function (err) {
                if (err) throw err;
                // you may respond with another html page
                newpath = '/"' + newpath + '/"';
                var command = 'sudo python ../../lightshowpi/py/synchronized_lights.py --file=' + newpath;
                cmd.run(command);
            });
        });
    }
}).listen(8086);
