
library(tidyverse)
library(showtext)
font_add_google("SulSans", "SulSans")
font_families()
showtext_auto() 

df <- read_csv('final-ifood-data.csv')
View(df)
df

head(df)
dim(df)
summary(df)

df %>% 
    filter(Nota == 5)

x <- df %>% 
    filter(Nota == 5) %>% 
    select(Título) %>% 
    c()

annotation = str_c(x[[1]][1], ' e ', x[[1]][2])
annotation

df %>% 
    filter(Nota > 0) %>% 
    ggplot(aes(x = Nota)) +
    geom_bar(fill = '#EA1D2C', color = '#F8F4E3') +
    geom_segment(aes(x = 5, y = 1.5, xend = 5, yend = 19.5, color = '#3F3E3E')) +
    annotate('text', label = annotation, x = 5, y = 21,
             hjust = 'right', fontface = 'bold', color = '#3F3E3E') +
    annotate('text', x = 5, y = 20.3, hjust = 'right', color = '#3F3E3E', size = 3,
             label = 'Únicos Restaurantes com nota 5 são do Emerson e do Marco') +
    labs(title = 'Distribuição das Notas\ndos Restaurantes',
         x = 'Nota', y = 'Frequência') +
    theme(plot.title = element_text(color = '#3F3E3E', size = 50, face = 'bold',
                                    family = 'Montserrat'),
          axis.title.x = element_text(color = '#EA1D2C', face = 'bold'),
          axis.title.y = element_text(color = '#3F3E3E'),
          legend.position = 'none'
          )

new_restaurants <- df %>% 
    filter(Nota == 0) %>% 
    nrow()

df %>% 
    filter(Nota < 3.5) %>% 
    arrange(desc(Nota))

df %>% 
    ggplot(aes(x = Preço)) +
    geom_histogram(bins = 10)


df %>% 
    mutate(Frete = ifelse(Preço <= 5, 'Barato', 'Caro')) %>% 
    group_by(Frete) %>% 
    summarise('Média das Notas' = mean(Nota))
# Pareçe que o preço do frete não é tão significante na Nota,
# as pessoas avaliam mais o sabor da comida

df %>% 
    ggplot(aes(y = Preço, x = Nota)) +
    geom_point()

df %>% 
    filter(Preço > 20, Nota > 4)

sum(df$Preço == 0)




df %>% 
    group_by(Tipo) %>% 
    summarise(Quantidade = n(), `Preço Médio` = mean(Preço),
              `Nota Média` = mean(Nota)) %>% 
    arrange(desc(`Nota Média`))

tipos_mais_frequentes <- df %>% 
    group_by(Tipo) %>% 
    summarise(Quantidade = n(), `Nota Média` = mean(Nota)) %>% 
    filter(Quantidade > 5) %>% 
    c()

df %>% 
    filter(Tipo %in% tipos_mais_frequentes[[1]]) %>% 
    ggplot(aes(x = Tipo, y = Nota)) +
    geom_boxplot()

df %>% 
    filter(Tipo %in% tipos_mais_frequentes[[1]]) %>% 
    ggplot(aes(x = Tipo, y = Preço)) +
    geom_boxplot()
    
getmode <- function(v) {
    uniqv <- unique(v)
    uniqv[which.max(tabulate(match(v, uniqv)))]
}
df %>% 
    group_by(Dono) %>% 
    summarise('Quantidade de Restaurantes' = n(),
              'Nota Média' = mean(Nota),
              'Tipo Mais Frequente' = getmode(Tipo),
              'Preço Médio' = mean(Preço))


