IMAGE=panel-demo:master

build:
	docker build -t $(IMAGE) .

push: build
	docker push $(IMAGE)

run: stop
	docker run -d -p 5006:5006 --name panel_demo $(IMAGE) 

stop:
	docker container rm -f panel_demo