import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers." )
   
    listToNpArray = np.array(list)

    npArray3x3 = listToNpArray.reshape(3, 3)

    meanAxis0 = npArray3x3.mean(axis=0)
    meanAxis1 = npArray3x3.mean(axis=1)
    meanFlattened = npArray3x3.mean()

    varAxis0 = npArray3x3.var(axis=0)
    varAxis1 = npArray3x3.var(axis=1)
    varFlattened = npArray3x3.var()

    stdAxis0 = npArray3x3.std(axis=0)
    stdAxis1 = npArray3x3.std(axis=1)
    stdFlattened = npArray3x3.std()

    maxAxis0 = npArray3x3.max(axis=0)
    maxAxis1 = npArray3x3.max(axis=1)
    maxFlattened = npArray3x3.max()

    minAxis0 = npArray3x3.min(axis=0)
    minAxis1 = npArray3x3.min(axis=1)
    minFlattened = npArray3x3.min()

    sumAxis0 = npArray3x3.sum(axis=0)
    sumAxis1 = npArray3x3.sum(axis=1)
    sumFlattened = npArray3x3.sum()

    calculations = {
        'mean' : [meanAxis0.tolist(), meanAxis1.tolist(), float(meanFlattened)],
        'variance' : [varAxis0.tolist(), varAxis1.tolist(), float(varFlattened)],
        'standard deviation' : [stdAxis0.tolist(), stdAxis1.tolist(), float(stdFlattened)],
        'max' : [maxAxis0.tolist(), maxAxis1.tolist(), int(maxFlattened)],
        'min' : [minAxis0.tolist(), minAxis1.tolist(), int(minFlattened)],
        'sum' : [sumAxis0.tolist(), sumAxis1.tolist(), int(sumFlattened)]
    }

   
    return calculations