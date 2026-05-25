from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer
from java.nio.IntBuffer import IntBuffer

class GLES31Ext:
    GL_BLEND_ADVANCED_COHERENT_KHR: ClassVar[int]
    GL_BUFFER_KHR: ClassVar[int]
    GL_CLAMP_TO_BORDER_EXT: ClassVar[int]
    GL_COLORBURN_KHR: ClassVar[int]
    GL_COLORDODGE_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR: ClassVar[int]
    GL_CONTEXT_FLAG_DEBUG_BIT_KHR: ClassVar[int]
    GL_DARKEN_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_FUNCTION_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_USER_PARAM_KHR: ClassVar[int]
    GL_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_SYNCHRONOUS_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_HIGH_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_LOW_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_MEDIUM_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_NOTIFICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_API_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_APPLICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_SHADER_COMPILER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_THIRD_PARTY_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_WINDOW_SYSTEM_KHR: ClassVar[int]
    GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_ERROR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_MARKER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PERFORMANCE_KHR: ClassVar[int]
    GL_DEBUG_TYPE_POP_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PORTABILITY_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PUSH_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_KHR: ClassVar[int]
    GL_DECODE_EXT: ClassVar[int]
    GL_DIFFERENCE_KHR: ClassVar[int]
    GL_EXCLUSION_KHR: ClassVar[int]
    GL_FIRST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_FRACTIONAL_EVEN_EXT: ClassVar[int]
    GL_FRACTIONAL_ODD_EXT: ClassVar[int]
    GL_FRAGMENT_INTERPOLATION_OFFSET_BITS_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_INPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_VERTICES_OUT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_BIT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_HARDLIGHT_KHR: ClassVar[int]
    GL_HSL_COLOR_KHR: ClassVar[int]
    GL_HSL_HUE_KHR: ClassVar[int]
    GL_HSL_LUMINOSITY_KHR: ClassVar[int]
    GL_HSL_SATURATION_KHR: ClassVar[int]
    GL_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_ISOLINES_EXT: ClassVar[int]
    GL_IS_PER_PATCH_EXT: ClassVar[int]
    GL_LAST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_LAYER_PROVOKING_VERTEX_EXT: ClassVar[int]
    GL_LIGHTEN_KHR: ClassVar[int]
    GL_LINES_ADJACENCY_EXT: ClassVar[int]
    GL_LINE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_MAX_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_MAX_DEBUG_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_LAYERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_LABEL_LENGTH_KHR: ClassVar[int]
    GL_MAX_PATCH_VERTICES_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_GEN_LEVEL_EXT: ClassVar[int]
    GL_MAX_TESS_PATCH_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MIN_SAMPLE_SHADING_VALUE_OES: ClassVar[int]
    GL_MULTIPLY_KHR: ClassVar[int]
    GL_OVERLAY_KHR: ClassVar[int]
    GL_PATCHES_EXT: ClassVar[int]
    GL_PATCH_VERTICES_EXT: ClassVar[int]
    GL_PRIMITIVES_GENERATED_EXT: ClassVar[int]
    GL_PRIMITIVE_BOUNDING_BOX_EXT: ClassVar[int]
    GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: ClassVar[int]
    GL_PROGRAM_KHR: ClassVar[int]
    GL_QUADS_EXT: ClassVar[int]
    GL_QUERY_KHR: ClassVar[int]
    GL_REFERENCED_BY_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT: ClassVar[int]
    GL_SAMPLER_KHR: ClassVar[int]
    GL_SAMPLE_SHADING_OES: ClassVar[int]
    GL_SCREEN_KHR: ClassVar[int]
    GL_SHADER_KHR: ClassVar[int]
    GL_SKIP_DECODE_EXT: ClassVar[int]
    GL_SOFTLIGHT_KHR: ClassVar[int]
    GL_STACK_OVERFLOW_KHR: ClassVar[int]
    GL_STACK_UNDERFLOW_KHR: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_STENCIL_INDEX_OES: ClassVar[int]
    GL_TESS_CONTROL_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_TESS_GEN_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_POINT_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_SPACING_EXT: ClassVar[int]
    GL_TESS_GEN_VERTEX_ORDER_EXT: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_BORDER_COLOR_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_SRGB_DECODE_EXT: ClassVar[int]
    GL_TRIANGLES_ADJACENCY_EXT: ClassVar[int]
    GL_TRIANGLE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_UNDEFINED_VERTEX_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_VERTEX_ARRAY_KHR: ClassVar[int]
    @staticmethod
    def glBlendBarrierKHR() -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(arg0: int, arg1: int, arg2: int, arg3: int, arg4: list[int], arg5: int, arg6: bool) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(arg0: int, arg1: int, arg2: int, arg3: int, arg4: IntBuffer, arg5: bool) -> None: ...
    @staticmethod
    def glDebugMessageInsertKHR(arg0: int, arg1: int, arg2: int, arg3: int, arg4: str) -> None: ...
    @staticmethod
    def glDebugMessageCallbackKHR(arg0: "DebugProcKHR") -> None: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(arg0: int, arg1: int, arg2: list[int], arg3: int, arg4: list[int], arg5: int, arg6: list[int], arg7: int, arg8: list[int], arg9: int, arg10: list[int], arg11: int, arg12: list[int], arg13: int) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer, arg5: IntBuffer, arg6: ByteBuffer) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(arg0: int, arg1: list[int], arg2: int, arg3: list[int], arg4: int, arg5: list[int], arg6: int, arg7: list[int], arg8: int) -> list[str]: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(arg0: int, arg1: IntBuffer, arg2: IntBuffer, arg3: IntBuffer, arg4: IntBuffer) -> list[str]: ...
    @staticmethod
    def glPushDebugGroupKHR(arg0: int, arg1: int, arg2: int, arg3: str) -> None: ...
    @staticmethod
    def glPopDebugGroupKHR() -> None: ...
    @staticmethod
    def glObjectLabelKHR(arg0: int, arg1: int, arg2: int, arg3: str) -> None: ...
    @staticmethod
    def glGetObjectLabelKHR(arg0: int, arg1: int) -> str: ...
    @staticmethod
    def glObjectPtrLabelKHR(arg0: int, arg1: str) -> None: ...
    @staticmethod
    def glGetObjectPtrLabelKHR(arg0: int) -> str: ...
    @staticmethod
    def glGetDebugMessageCallbackKHR() -> "DebugProcKHR": ...
    @staticmethod
    def glMinSampleShadingOES(arg0: float) -> None: ...
    @staticmethod
    def glTexStorage3DMultisampleOES(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool) -> None: ...
    @staticmethod
    def glCopyImageSubDataEXT(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> None: ...
    @staticmethod
    def glEnableiEXT(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glDisableiEXT(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendEquationiEXT(arg0: int, arg1: int) -> None: ...
    @staticmethod
    def glBlendEquationSeparateiEXT(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glBlendFunciEXT(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateiEXT(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...
    @staticmethod
    def glColorMaskiEXT(arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool) -> None: ...
    @staticmethod
    def glIsEnablediEXT(arg0: int, arg1: int) -> bool: ...
    @staticmethod
    def glFramebufferTextureEXT(arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @staticmethod
    def glPrimitiveBoundingBoxEXT(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> None: ...
    @staticmethod
    def glPatchParameteriEXT(arg0: int, arg1: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(arg0: int, arg1: int, arg2: list[int], arg3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(arg0: int, arg1: int, arg2: IntBuffer) -> None: ...
    @staticmethod
    def glTexBufferEXT(arg0: int, arg1: int, arg2: int) -> None: ...
    @staticmethod
    def glTexBufferRangeEXT(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> None: ...

    class DebugProcKHR:
        def onMessage(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str) -> None: ...
