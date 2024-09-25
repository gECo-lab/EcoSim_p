#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(data.table)
library(ggplot2)
library(dplyr)
library(tidyr)
library(jsonlite)


# Define server logic required to draw a histogram
function(input, output, session) {
  observeEvent(input$reset,{
    setwd(dirname(getActiveDocumentContext()$path))
    setwd("../")
  })
  
  output$out_dir <- renderPrint({
    setwd(input$dir)
    getwd()
  })
  
  #MODEL ####
  
  modelJsonContent <- reactiveVal(NULL)
  observeEvent(input$model, {
    req(input$model)
    
    # Read the uploaded file
    file <- input$model$datapath
    
    # Read JSON and store in reactive value
    jsonData <- fromJSON(file,simplifyDataFrame = F)
    modelJsonContent(jsonData)
    
    
  })
  
  observeEvent(input$model,{
    model <- modelJsonContent()
    types <- model$agents_classes
    output$agent_types <- renderUI({
      selectInput("agents_type_on","Agentes ativos",choices=types,selected = types,multiple = T)
    })
  })
  
  modelTemp <- reactive({
    model <- modelJsonContent()
    types <- model$agents_classes
    model_temp <- model
    model_temp$agents <- model_temp$agents[types %in% input$agents_type_on]
    model_temp
  })
  
  observeEvent(input$def_agents,{
    v <- list()
    model <- modelTemp()
    for (i in 1:length(model$agents)){
      v[[i]] <- box(width = 3,
                    numericInput(paste0("model_edit",i),
                                 label = model$agents[[i]]$agent_type,
                                 value = model$agents[[i]]$no_of_agents)
      )
    }
    output$model_boxes <- renderUI(v)
    
  })
  
  modelFinal <- reactive({
    model <- modelTemp()
    size <- length(model$agents)
    for (i in 1:length(model$agents)){
      eval(parse(text=paste0("model$agents[[i]]$no_of_agents <- input$model_edit",i )))
    }
    
    #pegar as edicoes e alterar
    model
  })
  
  output$out_model <- renderPrint({
    modelFinal()
    #input$agents_type_on
  }) 
  
  #SCENARIO ####
  scenarioJsonContent <- reactiveVal(NULL)
  observeEvent(input$scenario, {
    req(input$scenario)
    
    # Read the uploaded file
    file <- input$scenario$datapath
    
    # Read JSON and store in reactive value
    jsonData <- fromJSON(file,simplifyDataFrame = F)
    scenarioJsonContent(jsonData)
    
    
  })
  
  observeEvent(input$scenario,{
    scenarios_temp <- scenarioJsonContent()

    output$ui_no_of_runs <- renderUI({
      numericInput("no_of_runs","Number of runs",
                   value = scenarios_temp$scenarios[[1]]$scenario_parameters[[1]]$parameter_value,
                   min=1)
    })
    
    output$ui_reset_each_run <- renderUI({
      checkboxInput("reset_each_run","Reset each run",
                    value = scenarios_temp$scenarios[[1]]$scenario_parameters[[2]]$parameter_value)
    })
    
    output$ui_step_unit <- renderUI({
      textInput("step_unit","Step unit",
                value = scenarios_temp$scenarios[[1]]$scenario_parameters[[3]]$parameter_value)
    })
    
    output$ui_step_interval <- renderUI({
      numericInput("step_interval","Step interval",
                   value = scenarios_temp$scenarios[[1]]$scenario_parameters[[4]]$parameter_value,
                   min=1)
    })
    
    output$ui_no_of_steps <- renderUI({
      numericInput("no_of_steps","Number of Steps",
                   value = scenarios_temp$scenarios[[1]]$scenario_parameters[[5]]$parameter_value,
                   min=1)
    })
    
  })  
  
  scenarioFinal <- reactive({
    scenarios <- scenarioJsonContent()
    #no_of_runs
    scenarios$scenarios[[1]]$scenario_parameters[[1]]$parameter_value <- input$no_of_runs
    #reset_each_run
    scenarios$scenarios[[1]]$scenario_parameters[[2]]$parameter_value <- input$reset_each_run
    #step_unit
    scenarios$scenarios[[1]]$scenario_parameters[[3]]$parameter_value <- input$step_unit
    #step_interval
    scenarios$scenarios[[1]]$scenario_parameters[[4]]$parameter_value <- input$step_interval
    #no_of_steps
    scenarios$scenarios[[1]]$scenario_parameters[[5]]$parameter_value <- input$no_of_steps
    scenarios
  })
  
  output$out_scenario <- renderPrint({
    scenarioFinal()
  }) 
    
  #RUN ####
  observeEvent(input$run,{
    path <- "EcoSim_p-master_v2/"
    path2 <- "examples/ipd/"
    
    model_json <- toJSON(modelFinal(), pretty = TRUE, auto_unbox = TRUE)
    writeLines(model_json, paste0(path,path2,"models/model_temp.json"))
    
    scenarios_json <- toJSON(scenarioFinal(), pretty = TRUE, auto_unbox = TRUE)
    write_lines(scenarios_json, paste0(path,path2,"scenarios/scenarios_temp.json"))
    
    wd <- getwd()
    setwd("/cloud/project/EcoSim_p-master_v2")
    system2("python", args = c("ecosimp.py",
                               path2,
                               "config.json",
                               "models/model_temp.json",
                               "scenarios/scenarios_temp.json"))
    
    output$markdown <- renderUI({
      withMathJax(HTML(readLines(rmarkdown::render(input = "ipd.rmd",
                                                   output_format = rmarkdown::html_fragment(),
                                                   quiet = TRUE
      ))))
    })
    
    #p1 <- getwd()
    
    #do.call(file.remove, list(list.files("/cloud/project/EcoSim_p-master_v2/examples/ipd/runs",pattern = "*.csv", full.names = TRUE)))
    
    setwd("../")
    
  })
  
  observeEvent(input$clear,{
    setwd("/cloud/project/EcoSim_p-master_v2/examples/ipd/runs")
    list_runs <- list.files(pattern="*.csv")
    for (i in 1:length(list_runs)){
      file.remove(list_runs[i])
    }
    setwd("../../../../")
  })
  
}
