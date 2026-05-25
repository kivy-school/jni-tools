from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BluetoothLeScanner"]

class BluetoothLeScanner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/bluetooth/le/BluetoothLeScanner"
    EXTRA_CALLBACK_TYPE = JavaStaticField("Ljava/lang/String;")
    EXTRA_ERROR_CODE = JavaStaticField("Ljava/lang/String;")
    EXTRA_LIST_SCAN_RESULT = JavaStaticField("Ljava/lang/String;")
    startScan = JavaMultipleMethod([("(Landroid/bluetooth/le/ScanCallback;)V", False, False), ("(Ljava/util/List;Landroid/bluetooth/le/ScanSettings;Landroid/bluetooth/le/ScanCallback;)V", False, False), ("(Ljava/util/List;Landroid/bluetooth/le/ScanSettings;Landroid/app/PendingIntent;)I", False, False)])
    stopScan = JavaMultipleMethod([("(Landroid/bluetooth/le/ScanCallback;)V", False, False), ("(Landroid/app/PendingIntent;)V", False, False)])
    flushPendingScanResults = JavaMethod("(Landroid/bluetooth/le/ScanCallback;)V")