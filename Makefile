IMAGE=panel-demo:master

build:
	docker build -f MyDockerfile -t $(IMAGE) .

run: stop
	docker run -d -p 5006:5006 --name panel_demo $(IMAGE) 

stop:
	docker container rm -f panel_demo