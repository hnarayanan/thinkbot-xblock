$(document).ready(function() {

    jQuery.extend({
        getValues: function(url) {
            var result = null;
            $.ajax({
                url: url,
       		type: 'get',
       		dataType: 'json',
       		async: false,
       		success: function(data) {
                    result = data;
       		}
            });
            return result;
        }
    });

    jQuery.extend({


	renderValues: function(result, jobinfo, visualization) {
            var items = [];
            items.push('<ul>');
            items.push('<li><strong>Name:</strong> ' + result.name + '</li>');
            items.push('<li><strong>Owner:</strong> ' + result.owner + '</li>');
            items.push('<li><strong>Resource URL:</strong> ' + result.url + '</li>');
            items.push('<li><strong>Environment:</strong> ' + result.environment + '</li>');
            items.push('<li><strong>Requested results:</strong> ' + result.variables + '</li>');
            items.push('<li><strong>Status:</strong> ' + result.status + '</li>');
            items.push('<li><strong>Result URLs:</strong></br>')
            items.push('<ol>')
            $.each(result.results, function(key, val){
		items.push('<li>' + val + '</li>');
            });
            items.push('</ol>')
            items.push('</li>')
            items.push('</ul>');

            $(jobinfo).html(items.join(''));

            // create and initialize a 3D renderer
            var r = new X.renderer3D();
            r.container = visualization;
            r.init();
            r.camera.position = [0, 0, 2.5];
            r.camera.focus = [0, 0, 0];

            var solution = new X.mesh();
            solution.file = result.results[0];
            solution.magicmode = true;
            r.add(solution);
            r.render();
	}
    });

});
