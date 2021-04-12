FROM public.ecr.aws/lambda/python:3.8

RUN
COPY  ./

RUN python3.8 -m pip install -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["example.lambda.entry.lambda_handler"]
