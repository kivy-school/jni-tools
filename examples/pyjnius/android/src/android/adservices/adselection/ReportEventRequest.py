from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReportEventRequest"]

class ReportEventRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/adselection/ReportEventRequest"
    FLAG_REPORTING_DESTINATION_BUYER = JavaStaticField("I")
    FLAG_REPORTING_DESTINATION_COMPONENT_SELLER = JavaStaticField("I")
    FLAG_REPORTING_DESTINATION_SELLER = JavaStaticField("I")
    getInputEvent = JavaMethod("()Landroid/view/InputEvent;")
    getReportingDestinations = JavaMethod("()I")
    getKey = JavaMethod("()Ljava/lang/String;")
    getAdSelectionId = JavaMethod("()J")
    getData = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/adselection/ReportEventRequest$Builder"
        __javaconstructor__ = [("(JLjava/lang/String;Ljava/lang/String;I)V", False)]
        setAdSelectionId = JavaMethod("(J)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setInputEvent = JavaMethod("(Landroid/view/InputEvent;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setReportingDestinations = JavaMethod("(I)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setData = JavaMethod("(Ljava/lang/String;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        setKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/adselection/ReportEventRequest$Builder;")
        build = JavaMethod("()Landroid/adservices/adselection/ReportEventRequest;")