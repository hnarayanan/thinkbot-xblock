"""
The following XBlocks connect to the thinkbot compute service,
allowing students to carry out simulations in mathematical physics and
instructors to pose exercises within this context.
"""

from xblock.core import XBlock, Scope, Integer
from xblock.problem import InputBlock
from xblock.fragment import Fragment

import pkg_resources
import logging
log = logging.getLogger(__name__)


class ThinkbotSolutionBlock(XBlock):
    """
    An XBlock that allows students to interact with the results of a
    precomputed numerical solution. Such demonstrations are used to
    motivate the theoretical material covered in the classes.
    """

    id = Integer(help="ID of the simulation you'd like to display",
                    default=3, scope=Scope.content)
    width = Integer(help="Width of the visualization window",
                    default=500, scope=Scope.content)
    height = Integer(help="Height of the visualization window",
                     default=500, scope=Scope.content)

    def student_view(self, context):
        """
        Load HTML, CSS and JS from static templates and construct
        fragments to be returned.
        """

        html = pkg_resources.resource_string(__name__, "static/html/thinkbot_solution.html")
        fragments = Fragment(unicode(html) % {'id': self.id})

        css = pkg_resources.resource_string(__name__, "static/css/thinkbot_solution.css")
        fragments.add_css(unicode(css) % {'id': self.id, 'width': self.width, 'height': self.height})

        js = pkg_resources.resource_string(__name__, "static/js/thinkbot_solution.js")
        fragments.add_javascript_url("http://get.goXTK.com/xtk.js")
        fragments.add_javascript(unicode(js) % {'id': self.id})

        return fragments

    problem_view = student_view

    @staticmethod
    def workbench_scenarios():
        """
        A canned scenario for display in the workbench.
        """
        return [
            ("thinkbot solution",
             """\
             <vertical>
             <p>What follows is a solution of a nonlinear partial
             differential equation precomputed by <a
             href="http://thinkbot.net/">thinkbot</a>. Go on, play
             with the twisted hyperelastic block below!</p>
             <thinkbot_solution id="3" width="600" height="400" />
             <p>Such visualizations are used to motivate
             theoretical material covered in classes pertaining to
             applied mathematics and physical sciences. Soon,
             I&#8217;ll release the corresponding XBlock that <a
             href="http://mechanicsacademy.com/demo/thinkbot-api/">allows
             students to program numerical methods</a> for solving
             such equations themselves.</p>
             </vertical>
             """)
        ]


class ThinkbotExercise(InputBlock):
    """
    An XBlock that presents students with interactive and programming
    exercises tied to numerical simulation.
    """

    def student_view(self, context):
        pass
