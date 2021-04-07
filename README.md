## webcrawler-noticias
webcrawler para noticias selecionadas


### Docker comandos
    docker build -t webcrawler:v1 .

    docker run --name webcrawler-django -p 8080:8080 -d webcrawler:v1

    docker ps -a
    
    utils
    docker start webcrawler-django
    docker stop webcrawler-django
    docker exec -it webcrawler-django bash