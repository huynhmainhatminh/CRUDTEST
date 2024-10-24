using CRUDDATABASE.DAL;
using CRUDDATABASE.Repository;
using CRUDDATABASE.Repository.Implementations;
using Microsoft.EntityFrameworkCore;
using System;


namespace CRUDDATABASE
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            // Add services to the container.
            builder.Services.AddControllersWithViews();

			// DI

			builder.Services.AddScoped<IUnitOfWork, UnitOfWork>();

            //builder.Services.AddDbContext<ApptvcakoiContext>(
            //    options => options.UseMySql(builder.Configuration.GetConnectionString())
            //    );
            var connectionstring = builder.Configuration.GetConnectionString("MySqlConn");
            builder.Services.AddDbContext<ApptvcakoiContext>(options =>
            {
                options.UseMySql(connectionstring, ServerVersion.AutoDetect(connectionstring));
            });

            var app = builder.Build();

            // Configure the HTTP request pipeline.
            if (!app.Environment.IsDevelopment())
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }

            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthorization();

            app.MapControllerRoute(
                name: "default",
                pattern: "{controller=Home}/{action=Index}/{id?}");

            app.Run();
        }
    }
}
