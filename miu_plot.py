from fillplots import Plotter, annotate_regions
import matplotlib.pyplot as plt
import numpy as np

def miu_plot(list_lambdas,title="",axes_labels=("",""),xaxis=(-10,0),yaxis=(-10,0),
             show_legend=False,labels=[]):
    """
    Function for plotting chemical potential maps

    list_lambdas: list of lambda functions as tuple
                 [(lambda, True), (lambda, True)...] where True indicates "<" convention
    title: (string), title of plot
    axes_labels: list containing [x_axis_label,y_axis_label]
    xaxis, yaxis: containing min and max of axes
    label: tuple containing (xaxis_label, yaxis_label)
    show_legend: boolean for displaying legend
    labels: list of strings to label curves

    Inequalities follow "<" convention
    """

    # can plot multiple regions; in this case, list_lambdas bounds 1 region
    # automatic limits of axes implicitly includes chemical potential inequalities relating to elemental compounds
    # e.g., mu_O < 0

    plotter = Plotter([list_lambdas],xlim=xaxis,ylim=yaxis)


    #prettify the plot
    plt.xlabel(axes_labels[0],fontsize=14,labelpad=10)
    plt.ylabel(axes_labels[1],fontsize=14)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    if show_legend:
        i=0
        for ineq in plotter.regions[0].inequalities:
            ineq.boundary.config.line_args['label'] = labels[i]
            i=i+1

    # prettify inequality curves
    i=0; 
    for ineq in plotter.regions[0].inequalities:
        ineq.config.line_args = {'color': color_picker(i), 'linestyle':line_picker(i)}
        i=i+1
    plotter.plot()
    if show_legend:
        plotter.ax.legend(loc='best')

    return plotter

def color_picker(index):
  """ For when more control over colors is preferred 
      Cycles over the possible options """
  colors= ["royalblue","darkorange","darkgreen","darkcyan","k","cornflowerblue","crimson","indigo","darkmagenta","goldenrod","navy","slategray","olivedrab","saddlebrown"]
  index = np.mod(index,len(colors))
  return colors[index]

def line_picker(index):
  """ For when more control over line styles is preferred 
      Cycles over the possible options """

  lines = ['solid','dashed','dotted','dashdot']
  index = np.mod(index,len(lines))
  return lines[index]
