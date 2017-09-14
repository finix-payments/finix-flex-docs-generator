## Errors

Error Code | Meaning
---------- | -------
400 | Bad Request -- You've attemped an invalid request
401 | Unauthorized -- You have used the incorrect API key
402 | Upstream Processor Error -- Errors caused by 3rd party service
404 | Not Found -- The specified resource could not be found
422 | Unprocessable Entity -- The parameters were valid but the request failed. The error is usually some misunderstanding of various steps that have to be executed in order (e.g. attempting to initiate a transfer on behalf of a merchant that has not yet been approved)
500 | Internal Server Error -- We had a problem with our server. Try again later.
