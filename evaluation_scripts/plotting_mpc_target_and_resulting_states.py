"""
Author: Reuben Ferrante
Date:   10/05/2017
Description: General scripts for graphing instead of notebook.
"""

from evaluation_scripts.plotting_trajectory import *


def plot_single_trajectories(res):
    # Low Disc
    x_planned = np.load('')
    y_planned = np.load('')

    x_target = np.load('')
    y_target = np.load('')

    resulting_states = np.load('')


    fig = res.create_figure()
    ax = res.add_subplot(fig, 111, "X-Position/metres", "Z-Altitude/metres", grid=False)

    res.plot_graph(x_target, y_target, ax)
    res.plot_graph(x_target, y_target, ax, plottype='scatter')

    res.plot_graph(x_planned, y_planned, ax)
    res.plot_graph(x_planned, y_planned, ax, plottype='scatter')

    res.plot_graph(resulting_states[:-1, 0], resulting_states[:-1, 1], ax)
    res.plot_graph(resulting_states[:-1, 0], resulting_states[:-1, 1], ax, plottype='scatter')

    res.add_title('X-Z Target, Planned and Actual Trajectories for a Single Optimization Iteration')
    res.add_legend(['Target', 'Planned', 'Actual'])
    res.show_plot()

res = Graphing(plot_colors=None, fig_size=(8, 5))
plot_single_trajectories(res)