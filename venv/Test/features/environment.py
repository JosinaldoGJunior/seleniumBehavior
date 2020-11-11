from Packages.config_driver._ConfigDriver import ConfigDriver

def before_all(context):
    context.obj_driver = ConfigDriver().driver

def after_step(context,step):
    if step.status == 'failed':
        feature_arq = str(context.feature.name)
        name = 'scenario: ' + str(context.scenario.name) + ' step: ' + str(step.name) + ' = '
        status = str(step.status) + ' '
        print(name + status)
        context.obj_driver.save_screenshot("reports/screenshots/" + str(context.scenario.name) + "_" + str(step.name) + ".png")
    else:
        print(step.status, step.name)

def after_all(context):
    context.obj_driver.close()