from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillManager"]

class AutofillManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillManager"
    EXTRA_ASSIST_STRUCTURE = JavaStaticField("Ljava/lang/String;")
    EXTRA_AUTHENTICATION_RESULT = JavaStaticField("Ljava/lang/String;")
    EXTRA_AUTHENTICATION_RESULT_EPHEMERAL_DATASET = JavaStaticField("Ljava/lang/String;")
    EXTRA_CLIENT_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_INLINE_SUGGESTIONS_REQUEST = JavaStaticField("Ljava/lang/String;")
    notifyViewEntered = JavaMultipleMethod([("(Landroid/view/View;ILandroid/graphics/Rect;)V", False, False), ("(Landroid/view/View;)V", False, False)])
    requestAutofill = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;ILandroid/graphics/Rect;)V", False, False)])
    notifyViewExited = JavaMultipleMethod([("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;)V", False, False)])
    notifyViewClicked = JavaMultipleMethod([("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;)V", False, False)])
    notifyValueChanged = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;ILandroid/view/autofill/AutofillValue;)V", False, False)])
    showAutofillDialog = JavaMultipleMethod([("(Landroid/view/View;I)Z", False, False), ("(Landroid/view/View;)Z", False, False)])
    getUserDataId = JavaMethod("()Ljava/lang/String;")
    disableAutofillServices = JavaMethod("()V")
    getAutofillServiceComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getAvailableFieldClassificationAlgorithms = JavaMethod("()Ljava/util/List;")
    getDefaultFieldClassificationAlgorithm = JavaMethod("()Ljava/lang/String;")
    getNextAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    hasEnabledAutofillServices = JavaMethod("()Z")
    isAutofillSupported = JavaMethod("()Z")
    isFieldClassificationEnabled = JavaMethod("()Z")
    notifyViewVisibilityChanged = JavaMultipleMethod([("(Landroid/view/View;Z)V", False, False), ("(Landroid/view/View;IZ)V", False, False)])
    notifyVirtualViewsReady = JavaMethod("(Landroid/view/View;Landroid/util/SparseArray;)V")
    setUserData = JavaMethod("(Landroid/service/autofill/UserData;)V")
    commit = JavaMethod("()V")
    isEnabled = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    getUserData = JavaMethod("()Landroid/service/autofill/UserData;")
    registerCallback = JavaMethod("(Landroid/view/autofill/AutofillManager$AutofillCallback;)V")
    unregisterCallback = JavaMethod("(Landroid/view/autofill/AutofillManager$AutofillCallback;)V")

    class AutofillCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/autofill/AutofillManager$AutofillCallback"
        __javaconstructor__ = [("()V", False)]
        EVENT_INPUT_HIDDEN = JavaStaticField("I")
        EVENT_INPUT_SHOWN = JavaStaticField("I")
        EVENT_INPUT_UNAVAILABLE = JavaStaticField("I")
        onAutofillEvent = JavaMultipleMethod([("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;II)V", False, False)])