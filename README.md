# Kong Gateway

<img src="images/logo.png" width="5%" height="50%">

Este repositório tem como o objetivo entender o que é um API Gateway, procedimentos para instalação do Kong Gateway versão comunity (free) no Kubernetes e trazer alguns exemplos de utilização e configuração com o objetivo de explorar suas funcionalidades.

## Conteúdo

<!--ts-->
  * [Requisitos](#Requisitos)
  * [O que é um API Gateway](#O-que-é-um-API-Gateway)
  * [Kong Gateway](#Kong-Gateway)
  * [Topologias de Instalação do Kong](#Topologias-de-Instalação-do-Kong)
  * [Hands-On](#Hands-On)
    * [Mostrando o Ambiente](#Mostrando-o-Ambiente)
    * [Instalação Via Helm - Hybrid Mode](#Instalação-Via-Helm---Hybrid-Mode)
    * [Exemplos de Configurações](#Exemplos-de-Configurações)
      * [Via Web](#)
        * [Gateway Services](#)
        * [Routes](#)
        * [Consumers](#)
        * [Plugins](#)
      * [Via API](#)
        * [Gateway Services](#)
        * [Routes](#)
        * [Consumers](#)
        * [Plugins](#)
<!--te-->

## Requisitos:

* Um cluster Kubernetes na versão `>= v1.28.x`;
* Helm 3;
* Um Certificado SSL (opcional).

## O que é um API Gateway

<details>
É uma ferramenta de gerenciamento de API que atua entre o cliente (requisição) e uma gama de servidores (serviços), atua como um proxy reverso processando chamadas de API e as encaminhando para algum respectivo serviço em questão.

O processamento da requisição é baseado em políticas, que podem ser definidas no Path, Header, Query parameter da requisição e entre outros.

<img src="images/1.png" width="100%" height="50%">
</details>

## Kong Gateway

<details>

O [Kong Gateway](https://docs.konghq.com/gateway/3.6.x/#main) é um API Gateway desenvolvido em cima do Nginx com o foco em multi-cloud, arquiteturas distribuidas e otimizado para microserviços. Conhecido pela gama de configurações que podemos realizar no ambiente através de modulos e plugins. Então podemos integra-lo na frente de diversas aplicações REST ou HTTP.

Uns dos seus diferencias é a possibilidade de diversos tipos de instalações.

## Topologias de Instalação do Kong

O Kong Gateway possui diversas possibilidades de instalação, no link abaixo temos a documentação de todos os modos:

[Deployment Topologies](https://docs.konghq.com/gateway/3.6.x/production/deployment-topologies/)

</details>

## Hands-On

<details>
Agora iremos privionar um ambiente do Kong Gateway usando o modo de instalação Hybrid
</details>

### Instalação Via Helm - Hybrid Mode

<details>
</details>

### Exemplos de Configurações

<details>
</details>