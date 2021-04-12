FROM public.ecr.aws/lambda/python:3.8


COPY .tox/dist/*  ./
COPY example_lambda ./example_lambda
RUN ls -l
RUN python3.8 -m pip install ./hypergrowth* -t .


# Command can be overwritten by providing a different command in the template directly.
CMD ["example_lambda.entry.lambda_handler"]
