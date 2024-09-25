options(encoding = "UTF-8")

pacman::p_load(
  shiny,
  ggplot2,
  rmarkdown,
  rstudioapi,
  tidyr,
  dplyr,
  openxlsx,
  lubridate,
  stringi,
  stringr,
  GetBCBData,
  knitr,
  tis,
  shiny,
  shinyWidgets,
  plotly,
  tidyverse,
  plm,
  urca,
  DT,
  vars,
  tsDyn,
  shinyjs,
  jsonlite,
  shinymanager,
  fitdistrplus,
  shinydashboard,
  zoo,
  jsonlite
)

#devtools::install_github('wleepang/shiny-directory-input')
library(shiny)
library(shinyDirectoryInput)
library(shinyFiles)

setwd("../")
lista_pastas_arquivos <- list.files()

fluidPage(

  sidebarLayout(

    # sidebar ####
    sidebarPanel(
      selectInput("dir","Select EcoSim_p dir",choices=lista_pastas_arquivos),
      verbatimTextOutput("out_dir"),
      actionButton("reset","Reset"),
      fileInput("model","Choose model",accept = c(".json")),
      fileInput("scenario","Choose scenario",accept = c(".json")),
      actionButton("run","Run"),
      actionButton("clear","Clear Results")
    ),

    # mainbar ####
    mainPanel(
      tabsetPanel(
        ##aba modelo ####

        tabPanel(
          "Model",
          #selectizeInput("agent_types_on",options = c("",""),multiple=T),
          uiOutput("agent_types"),
          
          actionButton("def_agents","Editar Agentes"),
          fluidRow(
            tabPanel("Model",uiOutput("model_boxes"))
          ),
          verbatimTextOutput("out_model"),
          dataTableOutput("out_data_model"),
        ),

        
        
        
        
        ##aba cenarios ####
        tabPanel(
          "Scenario",
          uiOutput("ui_no_of_runs"),
          uiOutput("ui_reset_each_run"),
          uiOutput("ui_step_unit"),
          uiOutput("ui_step_interval"),
          uiOutput("ui_no_of_steps"),
          verbatimTextOutput("out_scenario")
                 ),

        ##aba visualizacao####
        tabPanel(
          "Output",
          
          uiOutput('markdown'),
          
          verbatimTextOutput("out_output")
        )
    )
  )

)
)