"""
The following XBlocks connect to the thinkbot compute service,
allowing students to carry out simulations in mathematical physics and
instructors to pose exercises within this context
"""

from xblock.core import XBlock
from xblock.problem import InputBlock
from xblock.fragment import Fragment

import logging
log = logging.getLogger(__name__)


class ThinkbotSimulation(XBlock):
    """
    An XBlock that allows students to interact with the results of a
    precomputed numerical solution. Such demonstrations are used to
    motivate the theoretical material covered in the classes.
    """

    def student_view(self, context):
        visualization = Fragment(u"""
        <h2>Visualizing the solution of a nonlinear partial
        differential equation</h2>
        <p>The results on this page are precomputed by <a
        href="http://thinkbot.net/">thinkbot</a>. Such demonstrations
        are used to motivate theoretical material covered by
        classes in applied mathematics and physical sciences.</p>
        <p>Go on, play with the solution field below!</p>
        <div id="visualization"></div>
        <div id="jobinfo"></div>
        <p>And head on over to <a
        href="http://mechanicsacademy.com/">Mechanics Academy</a> for
        more concrete examples of how they might be used in
        practice.</p>""")

        visualization.add_css("""
        #visualization {
          background-color:#000;
          width: 400px;
          height: 400px;
        }""")

        visualization.add_javascript_url("http://get.goXTK.com/xtk.js")
        visualization.add_javascript("""
        window.onload = function() {

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

          var renderValues = function(result, jobinfo, visualization) {
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

          result = $.getValues("http://api.thinkbot.net/jobs/4/");
	  renderValues(result, "#jobinfo", "visualization");

};



""")
        return visualization


class ThinkbotExercise(InputBlock):
    """
    An XBlock that presents students with interactive and programming
    exercises tied to numerical simulation.
    """

    def student_view(self, context):
        pass
