from prefect import flow


@flow(log_prints=True)
def flow_demo():
    print("I'm in a push pool. Is this like a push poll?")
    return "hi"
