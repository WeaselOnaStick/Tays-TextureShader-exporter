import bpy
from .export_operator import ExportShaderData

bl_info = {
    "name": "Tay's P3DXML texture & Shader Exporter (WOAS's fork)",
    "author": "WeaselOnaStick",
    "version": (0, 1, 0),
    "blender": (3, 0, 0),
    "wiki_url": "https://github.com/WeaselOnaStick/Tays-TextureShader-exporter/",
    "support": "COMMUNITY",
    "location": "File > Export",
    "category": "Import-Export",
}

def menu_func_export(self, context):
    self.layout.operator(ExportShaderData.bl_idname, icon="MATERIAL", text="Export textures & shaders (.p3dxml)")


def register():
    bpy.utils.register_class(ExportShaderData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportShaderData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
