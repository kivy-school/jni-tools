from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillManager"]

class AutofillManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/autofill/AutofillManager"
    EXTRA_ASSIST_STRUCTURE = JavaStaticField("Ljava/lang/String;")
    EXTRA_AUTHENTICATION_RESULT = JavaStaticField("Ljava/lang/String;")
    EXTRA_AUTHENTICATION_RESULT_EPHEMERAL_DATASET = JavaStaticField("Ljava/lang/String;")
    EXTRA_CLIENT_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_INLINE_SUGGESTIONS_REQUEST = JavaStaticField("Ljava/lang/String;")
    isEnabled = JavaMethod("()Z")
    requestAutofill = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;ILandroid/graphics/Rect;)V", False, False)])
    notifyViewEntered = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;ILandroid/graphics/Rect;)V", False, False)])
    notifyVirtualViewsReady = JavaMethod("(Landroid/view/View;Landroid/util/SparseArray;)V")
    notifyViewExited = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;I)V", False, False)])
    notifyViewVisibilityChanged = JavaMultipleMethod([("(Landroid/view/View;Z)V", False, False), ("(Landroid/view/View;IZ)V", False, False)])
    notifyValueChanged = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;ILandroid/view/autofill/AutofillValue;)V", False, False)])
    notifyViewClicked = JavaMultipleMethod([("(Landroid/view/View;)V", False, False), ("(Landroid/view/View;I)V", False, False)])
    commit = JavaMethod("()V")
    cancel = JavaMethod("()V")
    disableAutofillServices = JavaMethod("()V")
    hasEnabledAutofillServices = JavaMethod("()Z")
    getAutofillServiceComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getUserDataId = JavaMethod("()Ljava/lang/String;")
    getUserData = JavaMethod("()Landroid/service/autofill/UserData;")
    setUserData = JavaMethod("(Landroid/service/autofill/UserData;)V")
    isFieldClassificationEnabled = JavaMethod("()Z")
    getDefaultFieldClassificationAlgorithm = JavaMethod("()Ljava/lang/String;")
    getAvailableFieldClassificationAlgorithms = JavaMethod("()Ljava/util/List;")
    isAutofillSupported = JavaMethod("()Z")
    getNextAutofillId = JavaMethod("()Landroid/view/autofill/AutofillId;")
    registerCallback = JavaMethod("(Landroid/view/autofill/AutofillManager$AutofillCallback;)V")
    unregisterCallback = JavaMethod("(Landroid/view/autofill/AutofillManager$AutofillCallback;)V")
    showAutofillDialog = JavaMultipleMethod([("(Landroid/view/View;)Z", False, False), ("(Landroid/view/View;I)Z", False, False)])

    class AutofillCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/autofill/AutofillManager/AutofillCallback"
        __javaconstructor__ = [("()V", False)]
        EVENT_INPUT_HIDDEN = JavaStaticField("I")
        EVENT_INPUT_SHOWN = JavaStaticField("I")
        EVENT_INPUT_UNAVAILABLE = JavaStaticField("I")
        onAutofillEvent = JavaMultipleMethod([("(Landroid/view/View;I)V", False, False), ("(Landroid/view/View;II)V", False, False)])