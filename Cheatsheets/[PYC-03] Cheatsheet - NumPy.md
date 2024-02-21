# [PYC-03] Cheatsheet - NumPy

## Subsetting 1D arrays

* `arr[n]`: extracts the term of index `n` of the array `arr`. Since Python starts counting at zero, this would be the entry in place `n-1`.

* `arr[terms]`: extracts a subarray of the array `arr`, containing the terms whose index is in `terms`. This can be any vector-like object, such as a list, a range or a 1D array, with integer values.

* `arr[n:m]`: extracts a subarray containing the terms of `arr` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be equal to `0`. If `m` is missing, it is assumed to be equal to `len(arr)`.

* `arr[mask]`: extracts a subarray containing the terms for which `mask` takes value `True`. `mask` can be any vector-like object, such as list or a 1D array, with Boolean values (a Boolean mask) and the same length as `arr`.

## Subsetting 2D arrays

* `arr[n,m]`: extracts the term at row `n` and column `m`.

* `arr[r1:r2, c1:c2]`: extracts the subarray resulting from the selection of row indexes from `r1` to `r2-1` and column indexes from `c1` to `c2-1`.

* `arr[rows, c1:c2]`: extracts the subarray resulting from the selection of row indexes from `rows` and column indexes from `c1` to `c2-1`. `rows` can be any vector-like object, such as a list, a range or a 1D array, with integer values.

* `arr[mask, c1:c2]`: extracts the subarray resulting from the selection of row indexes for which `mask` takes value `True` and column indexes from `c1` to `c2-1`. `mask` can be any vector-like object, such as list or a 1D array, with Boolean values (a Boolean mask) and the same length as the number of rows of `arr`.

* `arr[r1:r2, cols]`: similar to `arr[rows, c1:c2]`.

* `arr[bm, c1:c2]`: similar to `arr[bm, c1:c2]`.

## NumPy attributes

* `.dtype`: returns the data type of an array. If the elements of that array are literals, it will be `int64`, `float64`, `<Ul` (`l` being the maximum length) or `bool`. More complex data can have data type `object`.

* `.ndim`: returns the number of dimensions, 1 for a 1D array and 2 for 2D array.

* `.shape`: returns the shape of the array, as a tuple. For a 1D array with `l` terms, it is `(l,)`, and, for a 2D array with `r` rows and `c` columns, `(r,c)`.

## NumPy methods 

* `.argmax()`: returns the index of the maximum term of an array. For a 2D array, the parameter `axis` allows for extracting the index of the maximum along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.argmin()`: returns the index of the minimum term of an array. For a 2D array, the parameter `axis` allows for extracting the index of the minimum along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.argsort()`: returns the indices that would sort an array, as a 1D array. For a 2D array, the parameter `axis` allows for extracting those indexes along rows (`axis=1`) or along columns (`axis=0`). With `axis=None`, it is applied to the flattened array. It takes some other less interesting keyword arguments.

* `.astype()`: converts an array to a specified data type. Takes one positional argument, specifying the new data type, plus some some less interesting keyword arguments. 

* `.corrcoef()`: returns the correlation matrix of a 2D array. With argument `rowvar=False` (the default) it calculates correlations of rows, with `rowvar=True`, correlations of columns. It can also take a list of numeric 1D arrays of the same length. 

* `.cumsum()`: for a 1D array, returns a 1D array containing the cumulative sums of the terms of the original array. For a 2D array, the cumulative sums are calculated row following row, but the parameter `axis` allows for cumulative sums along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.diagonal()`: extracts the diagonal of a square 2D array, as a 1D array. It takes some keyword arguments allowing for refinements.

* `.max()`: returns the maximum value of an array. For a 2D array, the parameter `axis` allows for extracting the maxima along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.mean()`: returns the mean value of an array. For a 2D array, the parameter `axis` allows for extracting the mean along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.min()`: returns the minimum value of an array. For a 2D array, the parameter `axis` allows for extracting the minima along rows (`axis=1`) or along columns (`axis=0`). It takes some other less interesting keyword arguments.

* `.reshape()`: returns an array containing the same data with a new shape. The number of terms of the reshaped array must be equal to that of the original array. The default of this method picks the elements to fill the new array by rows, from left to right. It takes positional arguments specifying the new shape (for a 2D array, the number of rows and the number of columns), plus a less interesting keyword argument.

* `.round(decimals=0)`: rounds the terms of a numeric array to a specified number of digits. It takes the (keyword) argument `decimals`, which defaults to zero, plus another less interesting keyword argument.

* `.sort()`: sorts a 1D array in ascending order *in place* (without returning the new version). Not the same as the function `sort()`. It can also be applied to 2D arrays. Look at the NumPy API Reference if you are interested.

* `.transpose()`: transposes a 2D array, turning rows into columns and columns into rows. `.T` is an abbreviation. It takes zero arguments.

## NumPy functions

* `np.abs()`: calculates the absolute values of an array, term by term.

* `np.arange(n, m, s)`: returns the same collection of integers as `range`, but as a 1D array.

* `np.argmax()`: the same as the method `.argmax()`.

* `np.argmin()`: the same as the method `.argmin()`.

* `np.array(values)`: if `values` is a vector-like object, such as a list or a range, it returns a 1D array containing the sames elements as `values`. If `values` is a list of vector-like objects of the same length, it returns a 2D array. The elements of `values` are coerced on the fly to a common type.

* `np.argsort()`: the same as the method `.argsort()`.

* `np.concatenate(arrlist)`: concatenates a list of arrays of the same number of dimensions, returning an array with that number of dimensions. For a list of 2D arrays, the parameter `axis` allows choosing between vertical (`axis=0`) and horizontal (`axis=1`) concatenation. The default is `axis=0`. It takes some other keyword arguments whose default you will never change.

* `np.corrcoef()`: the same as the method `.corrcoef()`. As a function, it can be applied to a list of 1D arrays.

* `np.cumsum()`: the same as the method `.cumsum()`.

* `np.delete(arr, lst)`: for a 1D array, deletes the terms of the array `arr` whose indexes are in the list `lst`. It returns the complement of `arr[lst]`. `lst` can also be a single index, or a range. For a 2D array, an axis can be specified. With `axis=0`, it deletes rows and, with `axis=1`, columns, and with `axis=None` (the default) it applies to the flattened array.  It takes two positional arguments plus the (keyword) `axis` argument.

* `np.diagonal()`: the same as the method `.diagonal()`.

* `np.int64()`: the same as the method `.astype('int')`.

* `np.float64()`: the same as the method `.astype('float')`.

* `np.linspace(start, stop, num=50)`: returns evenly spaced numbers over a specified interval. It takes to positional arguments plus the (keyword) `num` argument which defaults to 50.

* `np.max()`: the same as the method `.max()`.

* `np.mean()`: the same as the method `.mean()`.

* `np.min()`: the same as the method `.min()`.

* `np.ones(shape)`: creates an array with dimensions given by `shape`, filled with ones.
  
* `np.reshape()`: the same as the method `.reshape()`.

* `np.round()`: the same as the method `.round()`.

* `np.sort()`: sorts a 1D array in ascending order. Not the same as the method `.sort()`.

* `np.stack(arrlist, axis=0)`: joins a list of arrays of the same dimensions, returning an array with an extra axis. For instance, if `arr1` and `arr2` are two vectors of the same length, `np.stack([arr1, arr2])` puts them as the rows of a matrix, while `np.stack([arr1, arr2], axis=1)` puts them as the columns of a matrix. Note that `np.stack()` increases the number of dimensions, while `np.concatenate()` leaves it unchanged.

* `np.sum()`: the same as the method `.sum()`.

* `np.transpose()`: the same as the method `.transpose()`. 

* `np.unique(arr, return_counts=False)`: returns the sorted (ascending) unique terms of the array specified by the parameter `ar`. With the keyword argument `returns_counts=True` (not the default), it returns also an array containing the number of occurrences of every unique value. It has other parameters whose default you will never change. 

* `np.vectorize()`: vectorizes a function, so it can take vector-like objects, such as lists or 1D arrays, as arguments. Irrespective of the type of those objects, a vectorized function always returns a NumPy array.
  
* `np.zeros(shape)`: creates an array with dimensions given by `shape`, filled with zeros.
