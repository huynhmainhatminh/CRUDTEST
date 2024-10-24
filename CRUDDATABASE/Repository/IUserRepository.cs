using CRUDDATABASE.DAL;

namespace CRUDDATABASE.Repository
{
    public interface IUserRepository
    {
        Task<IEnumerable<QlUser>> GetUsers();
        Task<QlUser> GetUserById(int id);
        Task Add(QlUser user);
        Task Update(QlUser user);
        Task Delete(int id);
    }
}
