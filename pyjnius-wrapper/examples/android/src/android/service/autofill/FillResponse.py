from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillResponse"]

class FillResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_DELAY_FILL = JavaStaticField("I")
    FLAG_DISABLE_ACTIVITY_ONLY = JavaStaticField("I")
    FLAG_TRACK_CONTEXT_COMMITED = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/autofill/FillResponse/Builder"
        __javaconstructor__ = [("()V", False)]
        setDetectedFieldClassifications = JavaMethod("(Ljava/util/Set;)Landroid/service/autofill/FillResponse$Builder;")
        setAuthentication = JavaMultipleMethod([("([Landroid/view/autofill/AutofillId;Landroid/content/IntentSender;Landroid/widget/RemoteViews;)Landroid/service/autofill/FillResponse$Builder;", False, False), ("([Landroid/view/autofill/AutofillId;Landroid/content/IntentSender;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/FillResponse$Builder;", False, False), ("([Landroid/view/autofill/AutofillId;Landroid/content/IntentSender;Landroid/widget/RemoteViews;Landroid/service/autofill/InlinePresentation;Landroid/service/autofill/InlinePresentation;)Landroid/service/autofill/FillResponse$Builder;", False, False), ("([Landroid/view/autofill/AutofillId;Landroid/content/IntentSender;Landroid/service/autofill/Presentations;)Landroid/service/autofill/FillResponse$Builder;", False, False)])
        setIgnoredIds = JavaMethod("([Landroid/view/autofill/AutofillId;)Landroid/service/autofill/FillResponse$Builder;", varargs=True)
        addDataset = JavaMethod("(Landroid/service/autofill/Dataset;)Landroid/service/autofill/FillResponse$Builder;")
        setSaveInfo = JavaMethod("(Landroid/service/autofill/SaveInfo;)Landroid/service/autofill/FillResponse$Builder;")
        setClientState = JavaMethod("(Landroid/os/Bundle;)Landroid/service/autofill/FillResponse$Builder;")
        setFieldClassificationIds = JavaMethod("([Landroid/view/autofill/AutofillId;)Landroid/service/autofill/FillResponse$Builder;", varargs=True)
        setFlags = JavaMethod("(I)Landroid/service/autofill/FillResponse$Builder;")
        disableAutofill = JavaMethod("(J)Landroid/service/autofill/FillResponse$Builder;")
        setIconResourceId = JavaMethod("(I)Landroid/service/autofill/FillResponse$Builder;")
        setServiceDisplayNameResourceId = JavaMethod("(I)Landroid/service/autofill/FillResponse$Builder;")
        setShowFillDialogIcon = JavaMethod("(Z)Landroid/service/autofill/FillResponse$Builder;")
        setShowSaveDialogIcon = JavaMethod("(Z)Landroid/service/autofill/FillResponse$Builder;")
        setHeader = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/FillResponse$Builder;")
        setFooter = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/FillResponse$Builder;")
        setUserData = JavaMethod("(Landroid/service/autofill/UserData;)Landroid/service/autofill/FillResponse$Builder;")
        setPresentationCancelIds = JavaMethod("([I)Landroid/service/autofill/FillResponse$Builder;")
        setDialogHeader = JavaMethod("(Landroid/widget/RemoteViews;)Landroid/service/autofill/FillResponse$Builder;")
        setFillDialogTriggerIds = JavaMethod("([Landroid/view/autofill/AutofillId;)Landroid/service/autofill/FillResponse$Builder;", varargs=True)
        build = JavaMethod("()Landroid/service/autofill/FillResponse;")