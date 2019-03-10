from sklearn.metrics import confusion_matrix

def tp(y_true, y_pred): return confusion_matrix(y_true, y_pred).ravel()[3]
def tn(y_true, y_pred): return confusion_matrix(y_true, y_pred).ravel()[0]
def fp(y_true, y_pred): return confusion_matrix(y_true, y_pred).ravel()[1]
def fn(y_true, y_pred): return confusion_matrix(y_true, y_pred).ravel()[2]


def specificity(y_true, y_pred):
    if tn(y_true, y_pred) + fp(y_true, y_pred) == 0:
        return 0
    else:
        return float(tn(y_true, y_pred)) / float((tn(y_true, y_pred) + fp(y_true, y_pred)))


def f1(y_true, y_pred):
    return 2 * (precision(y_true, y_pred) * sensitivity(y_true, y_pred)) / (precision(y_true, y_pred) +
                                                                            sensitivity(y_true, y_pred))


def sensitivity(y_true, y_pred):
    if tp(y_true, y_pred) + fn(y_true, y_pred) == 0:
        return 0
    else:
        return float(tp(y_true, y_pred)) / float((tp(y_true, y_pred) + fn(y_true, y_pred)))


def precision(y_true, y_pred):
    return tp(y_true, y_pred) / (tp(y_true, y_pred) + fp(y_true, y_pred))


def accuracy(y_true, y_pred):
    return (tp(y_true, y_pred) + tn(y_true, y_pred)) / ((tp(y_true, y_pred) + tn(y_true, y_pred) + fp(y_true, y_pred)
                                                         + fn(y_true, y_pred)))

